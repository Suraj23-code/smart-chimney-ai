# Smart Chimney AI v2 prototype

## Run locally
1. Install Python 3.10+.
2. Extract this ZIP and open a terminal in the folder.
3. Run: `pip install -r requirements.txt`
4. Run: `python app.py`
5. Open: http://127.0.0.1:5000

## Included
- Dark industrial dashboard
- Interactive factory and pollutant sliders
- Random Forest demo prediction API
- Live current/predicted graphs and session analytics
- Normal, rising-pollution and critical scenario presets
- Virtual ESP, scrubber, servo damper and filtration recommendations
- Browser geolocation with map link
- Browser notifications (permission required)
- Voice commands and spoken responses (browser support varies)
- Adaptive energy index comparison

## Important limitations
All sensor readings and training data are synthetic. The forecast is a demonstration next-step estimate, not a validated 5–15 minute prediction. Thresholds are illustrative, not legal limits. Energy values are an index, not measured consumption. No physical equipment is connected. Location and voice require browser permission; use localhost or HTTPS. Real deployment requires calibrated sensors, real plant data, engineering validation, safety interlocks and regulatory review.
