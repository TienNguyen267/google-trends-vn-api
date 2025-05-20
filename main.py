from flask import Flask, jsonify
from flask_cors import CORS
from pytrends.request import TrendReq
import os

app = Flask(__name__)
CORS(app)
pytrends = TrendReq(hl='vi-VN', tz=420)

@app.route('/trends/vn')
def trends_vn():
    try:
        trending_searches = pytrends.trending_searches(pn='vietnam')
        queries = [item.get("title", "") for item in trending_searches["storySummaries"]["trendingStories"]]
        return jsonify(queries[:10])
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
