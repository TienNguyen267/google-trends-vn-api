from fastapi import FastAPI
from pytrends.request import TrendReq
from fastapi.middleware.cors import CORSMiddleware

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
        pytrends = TrendReq()
        data = pytrends.trending_searches(pn=region.lower())
        return {"trends": data[0].tolist()}
    except Exception as e:
        return {"error": str(e)}
