#Importing Librarie
import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

#Downlaoding Data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2)


pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('classifier', RandomForestClassifier(n_estimators=50, max_depth=3, random_state=42))
])

with mlflow.start_run():
    pipeline.fit(X_train, y_train)
    predictions = pipeline.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    mlflow.log_param("n_estimators", 50)
    mlflow.log_param("max_depth", 3)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(pipeline, "model", skops_trusted_types=["sklearn.tree._tree.Tree"])
    
    