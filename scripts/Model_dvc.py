import yaml
import json
import pandas as pd
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, f1_score, precision_score, recall_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import joblib


with open('params.yaml', 'r') as f:
    params = yaml.safe_load(f) 
###Dir
df=pd.read_csv("/Users/alejandraossayepes/Library/CloudStorage/OneDrive-MIC/00_Maestria/14 Proyecto_1/Modulo_3/proyecto-prediccion-diabtes/proyecto-prediccion-diabtes/data/raw/diabetes.csv")
print('Cant_reg', df.shape)
target_name='Outcome'
y= df[target_name]
X=df.drop(target_name,axis=1)
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.2,random_state=0)


# KNN
knn = KNeighborsClassifier()
knn_grid = GridSearchCV(estimator=knn, param_grid=params['knn'], cv=RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1), scoring='f1', n_jobs=-1, error_score=0)
knn_grid.fit(X_train, y_train)
knn_pred = knn_grid.predict(X_test)
joblib.dump(knn_grid.best_estimator_, 'models/knn_model.pkl')
print('KNN model saved')

# Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt_grid = GridSearchCV(estimator=dt, param_grid=params['decision_tree'], cv=4, n_jobs=-1, verbose=1, scoring='accuracy')
dt_grid.fit(X_train, y_train)
dt_pred = dt_grid.predict(X_test)
joblib.dump(dt_grid.best_estimator_, 'models/dt_model.pkl')
print('DT model saved')


# Random Forest
rf = RandomForestClassifier()
rf_grid = GridSearchCV(estimator=rf, param_grid=params['random_forest'], cv=RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1), scoring='accuracy', n_jobs=-1, error_score=0)
rf_grid.fit(X_train, y_train)
rf_pred = rf_grid.predict(X_test)
joblib.dump(rf_grid.best_estimator_, 'models/rf_model.pkl')
print('RF model saved')

# Evaluación
def evaluate_model(y_true, y_pred, model_name):
    metrics = {
            "f1_score": f1_score(y_true, y_pred),
            "precision": precision_score(y_true, y_pred),
            "recall": recall_score(y_true, y_pred)
        }
    print(f"Classification Report for {model_name}:\n", classification_report(y_true, y_pred))
    print(f"\n F1 Score for {model_name}:\n", f1_score(y_true, y_pred))
    print(f"\n Precision Score for {model_name}:\n", precision_score(y_true, y_pred))
    print(f"\n Recall Score for {model_name}:\n", recall_score(y_true, y_pred))
    print(f"\n Confusion Matrix for {model_name}:\n")
    sns.heatmap(confusion_matrix(y_true, y_pred))
    plt.show()

    # Guardar métricas en un archivo JSON
    with open(f'data/results/{model_name}_metrics.json', 'w') as f:
        json.dump(metrics, f, indent=4)

evaluate_model(y_test, knn_pred, 'KNN')
evaluate_model(y_test, dt_pred, 'Decision Tree')
evaluate_model(y_test, rf_pred, 'Random Forest') 