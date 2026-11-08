import os
import mlflow.sklearn
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI(title="ML Pipeline API")

# 1. تحديد مكان الملف الحالي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. المسار الدقيق (تمت إضافة "artifacts" في النهاية بناءً على مسار الصورة الدقيق)
model_path = os.path.join(BASE_DIR, "mlruns", "0", "models", "m-d5046dc3baa347a79fe5d2e546d90096", "artifacts")

# 3. تحميل الموديل
model = mlflow.sklearn.load_model(f"file://{model_path}")

# 4. إعدادات البيانات
class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# 5. مسار التنبؤ
@app.post("/predict")
def predict(data: IrisData):
    input_data = pd.DataFrame([data.model_dump()])
    prediction = model.predict(input_data)
    return {"flower_class_prediction": int(prediction[0])}