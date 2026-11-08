# 🌸 Iris Flower Classifier: My ML Deployment Journey

Hey there!  Welcome to my machine learning deployment project. 

I built this application to do one simple but cool thing: predict the exact species of an Iris flower based on its petal and sepal measurements. But more importantly, this project was my playground for tying together a complete, end-to-end ML pipeline—from tracking the model to serving it via an API, and finally wrapping it all in a neat Docker container so anyone can run it without the dreaded *"it works on my machine"* excuse! 

## 🛠️ What I Used to Build This (Tech Stack)

*   **FastAPI:** For the backend API (because it's incredibly fast and developer-friendly).
*   **Streamlit:** For the frontend (makes building interactive UIs for ML models a breeze).
*   **MLflow:** To track my model experiments and manage the saved artifacts.
*   **Docker & Docker Compose:** To containerize the whole thing and make it run anywhere with a single command.

## ⚙️ How the Magic Happens

1. You open the **Streamlit** app in your browser and play around with the sliders to set the flower's measurements.
2. Once you hit predict, the frontend knocks on the **FastAPI** backend's door (using Docker's internal network).
3. The backend wakes up the pre-trained Scikit-Learn model (managed by **MLflow**), calculates the prediction, and sends the result right back to your screen.

## 🚀 Want to try it out? 

It's super easy to run this locally. You just need to have [Docker](https://docs.docker.com/get-docker/) installed.

**1. Clone this repo:**
```bash
git clone [https://github.com/redxnooy-sys/ML-Flow-Project.git](https://github.com/redxnooy-sys/ML-Flow-Project.git)
cd ML-Flow-Project
