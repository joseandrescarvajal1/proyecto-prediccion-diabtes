from fastapi import FastAPI, HTTPException, Header, status, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import joblib
from dotenv import load_dotenv
import os
load_dotenv()


model_path = os.getenv("model_name")


app = FastAPI()

class Item(BaseModel):
    edad: int 
    glucosa: float
    grosor_piel: float
    bmi : float
    presion_sanguinea: float
    embarazos:int
    insulina: float
    pedigree: float

   
@app.get("/predict/")

def predict(item: Item):
    model =  joblib.load(f'models/{model_path}')

    ddata  = [item.embarazos, item.glucosa, item.presion_sanguinea, item.grosor_piel, item.insulina, item.bmi, item.pedigree, item.edad]
    prediction = int(model.predict([ddata])[0])

    print(prediction)
    return JSONResponse(content={'prediction': prediction}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)