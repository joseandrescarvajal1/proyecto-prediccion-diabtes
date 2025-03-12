import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import warnings #avoid warning flash
warnings.filterwarnings('ignore')
from sklearn.model_selection import train_test_split
import mlflow
import mlflow.sklearn
from models import *


df=pd.read_csv("data/raw/diabetes.csv")
target_name='Outcome'
y= df[target_name]
X=df.drop(target_name,axis=1)



X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2,random_state=0)
# best_model, best_params = train_knn(X_train, y_train)
# best_model, best_params = train_random_forest(X_train, y_train)
best_model, best_params = train_descion_tree(X_train, y_train)


f1, precision, recall = model_predict(X_test, y_test, best_model)

experiment_name = "diabetes_experiments"
# mlflow.create_experiment(experiment_name)
experiment = mlflow.set_experiment(experiment_name)

with mlflow.start_run(experiment_id=experiment.experiment_id):
    for key, value in best_params.items():
        mlflow.log_param(key, value)
    mlflow.log_metric("f1", f1)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.sklearn.log_model(best_model, "model")

