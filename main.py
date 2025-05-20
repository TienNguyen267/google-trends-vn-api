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
        data = pytrends.trending_searches(pn='vietnam')
        return jsonify(data[0:10].tolist())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
