from fastapi import FastAPI, Form
import util
from fastapi.middleware.cors import CORSMiddleware
from typing import Annotated

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/get_location_names')
async def get_location_names():
    return {
        'locations': util.get_location_names()
    }

@app.post("/predict_home_price")
async def predict_home_price(
    total_sqft: Annotated[float, Form(...)],
    bhk:  Annotated[int, Form(...)],
    bath: Annotated[int, Form(...)],
    location: Annotated[str, Form(...)]):

    return{
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    }

if __name__ == "__main__":
    print("Starting Python Fastapi Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()   