from flask import Flask, jsonify
from pytrends.request import TrendReq
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

pytrends = TrendReq(hl='vi-VN', tz=420)

@app.route('/trends/vn')
def trends_vn():
    try:
        trending_searches = pytrends.trending_searches(pn='vietnam')
        return jsonify(trending_searches[0:10].tolist())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)