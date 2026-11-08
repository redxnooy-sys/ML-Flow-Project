import streamlit as st
import requests


st.set_page_config(page_title="Predict Flower Type", page_icon="🌸")

st.write(" ")
st.title("IRIS flower Predict ")

col1, col2 = st.columns(2)

with col1 :
  sepal_length = st.number_input("sepal_length (sepal_length): ", min_value=0.0, value=5.1, step=0.1)
  sepal_width = st.number_input("sepal_width (sepal_width): ", min_value=0.0, value=0.2, step=0.1)
with col2:
 petal_length = st.number_input("petal_length (petal_length): ", min_value=0.0, value=1.4, step=0.1)
petal_width = st.number_input("petal_width (petal_width):",min_value=0.0, value=0.2, step=0.1)


iris_info = {
    0: {
        "name": "Iris Setosa ", 
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg"
    },
    1: {
        "name": "Iris Versicolor ", 
        "image": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg"
    },
    2: {
        "name": "Iris Virginica ", 
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg"
    }
}

if st.button("Predict Flower Type "):



 user_data = {
    "sepal_length": sepal_length,
    "sepal_width": sepal_width,
    "petal_length": petal_length,
    "petal_width": petal_width
}
 
 API_URL = "http://backend:8000/predict"
 try:
    with st.spinner(''):
      response = requests.post(API_URL, json=user_data)
    
    
    if response.status_code == 200:
        result = response.json()
        flower_class_number = int(result["flower_class_prediction"])

        if flower_class_number in iris_info :
           flower_name = iris_info[flower_class_number]["name"]
           flower_image_url = iris_info[flower_class_number]["image"]
           st.image(flower_image_url, caption=f"Flower  {flower_name}", width='stretch')
           st.header(f"NAME  : {flower_name} ")
    else:
        print(" API Error")
 except Exception as e:
    print(f"\n FastAPI Error {e}")






