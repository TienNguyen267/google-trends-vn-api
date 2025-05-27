from fastapi import FastAPI
from pytrends.request import TrendReq
from fastapi.middleware.cors import CORSMiddleware
import traceback

app = FastAPI()
pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25), retries=2, backoff_factor=0.1)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/trends/global")
def get_global_trends():
    try:
        data = pytrends.trending_searches()
        return {"trends": data[0].tolist()}
    except Exception as e:
        print("Error in /trends/global:")
        print(traceback.format_exc())
        return {"error": str(e)}

@app.get("/related/{keyword}")
def get_related_queries(keyword: str):
    try:
        pytrends.build_payload([keyword], geo='')
        results = pytrends.related_queries()
        related = results.get(keyword, {})
        return {
            "top": related.get("top", {}).to_dict(orient="records") if related.get("top") is not None else [],
            "rising": related.get("rising", {}).to_dict(orient="records") if related.get("rising") is not None else []
        }
    except Exception as e:
        print("Error in /related/{keyword}:")
        print(traceback.format_exc())
        return {"error": str(e)}
