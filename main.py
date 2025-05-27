from fastapi import FastAPI
from pytrends.request import TrendReq
from fastapi.middleware.cors import CORSMiddleware
import traceback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/trends/{region}")
def get_trends(region: str):
    try:
        pytrends = TrendReq(hl='en-US', tz=360, timeout=(10, 25), retries=2, backoff_factor=0.1)
        data = pytrends.trending_searches(pn=region.lower())
        return {"trends": data[0].tolist()}
    except Exception as e:
        print("Error while fetching trends:")
        print(traceback.format_exc())
        return {"error": str(e)}
