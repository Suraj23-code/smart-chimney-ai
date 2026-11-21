from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.multioutput import MultiOutputRegressor
app=Flask(__name__)
rng=np.random.default_rng(17); n=5000
s=rng.uniform(0,150,n); no=rng.uniform(0,150,n); pm=rng.uniform(0,150,n)
load=rng.uniform(10,100,n); temp=rng.uniform(15,55,n); hum=rng.uniform(15,95,n)
X=np.c_[s,no,pm,load,temp,hum]
Y=np.c_[np.maximum(0,s+.23*(load-50)+.14*(temp-30)+rng.normal(0,5,n)),
        np.maximum(0,no+.27*(load-50)+.11*(temp-30)+rng.normal(0,5,n)),
        np.maximum(0,pm+.20*(load-50)-.06*(hum-50)+rng.normal(0,6,n))]
model=MultiOutputRegressor(RandomForestRegressor(n_estimators=80,max_depth=12,min_samples_leaf=3,random_state=17,n_jobs=-1)).fit(X,Y)
@app.get("/")
def home(): return render_template("index.html")
@app.post("/api/predict")
def predict():
 d=request.get_json(force=True); v=[float(d[k]) for k in ["so2","no2","pm25","load","temp","humidity"]]
 p=np.maximum(0,model.predict([v])[0]); limits=[80,80,75]
 ratios=[v[i]/limits[i] for i in range(3)]+[p[i]/limits[i] for i in range(3)]
 r=max(ratios); risk="CRITICAL" if r>=1 else "ELEVATED" if r>=.75 else "NORMAL"
 filt=100 if risk=="CRITICAL" else int(np.clip(25+65*min(r,1.5)/1.5,25,90))
 return jsonify(prediction=dict(so2=round(float(p[0]),1),no2=round(float(p[1]),1),pm25=round(float(p[2]),1)),
 risk=risk,filtration=filt,pump="ON – high demand" if max(p[0]/80,p[1]/80)>=.75 else "LOW / STANDBY",
 esp="HIGH" if max(v[2]/75,p[2]/75)>=.75 else "NORMAL",
 damper="Priority treatment path" if risk!="NORMAL" else "Normal treatment path",
 energy_index=filt,energy_saved=max(0,100-filt))
if __name__=="__main__": app.run(host="127.0.0.1",port=5000,debug=True)
