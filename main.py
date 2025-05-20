from flask import Flask, jsonify
from flask_cors import CORS
from pytrends.request import TrendReq
import os
import traceback

app = Flask(__name__)
CORS(app)

pytrends = TrendReq(hl='vi-VN', tz=420)

@app.route('/trends/vn')
def trends_vn():
    try:
        df = pytrends.realtime_trending_searches(pn='VN')  # ✅ Cái này hoạt động
        top_titles = df["title"].dropna().tolist()[:10]     # Lấy danh sách top 10 title
        return jsonify(top_titles)
    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
