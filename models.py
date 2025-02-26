from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


def train_knn(x_train, y_train):
    knn= KNeighborsClassifier()
    n_neighbors = list(range(15,25))
    p=[1,2]
    weights = ['uniform', 'distance']
    metric = ['euclidean', 'manhattan', 'minkowski']
    hyperparameters = dict(n_neighbors=n_neighbors, p=p,weights=weights,metric=metric)
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    grid_search = GridSearchCV(estimator=knn, param_grid=hyperparameters, n_jobs=-1, cv=cv, scoring='f1',error_score=0)
    best_model = grid_search.fit(x_train,y_train)
    return best_model, grid_search.best_params_

def train_descion_tree(x_train, y_train):

    max_depth = [5, 10, 20, 25]
    min_samples_leaf =  [10, 20, 50, 100, 120]
    criterion =  ['gini', 'entropy']
    hyperparameters = dict(max_depth=max_depth, min_samples_leaf=min_samples_leaf,criterion=criterion)
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    grid_search = GridSearchCV(estimator=DecisionTreeClassifier(), param_grid=hyperparameters, n_jobs=-1, cv=cv, scoring='f1',error_score=0)
    best_model = grid_search.fit(x_train,y_train)
    return best_model, grid_search.best_params_

def train_random_forest(x_train, y_train):
    n_estimators =  [1800]
    max_features = ['sqrt', 'log2']
    hyperparameters = dict(n_estimators=n_estimators, max_features=max_features)
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    grid_search = GridSearchCV(estimator=RandomForestClassifier(), param_grid=hyperparameters, n_jobs=-1, cv=cv, scoring='f1',error_score=0)
    best_model = grid_search.fit(x_train,y_train)
    return best_model, grid_search.best_params_

def model_predict(x_test,y_test, best_model):
    y_pred = best_model.predict(x_test)
    f1 = f1_score(y_test,y_pred)
    precision = precision_score(y_test,y_pred)
    recall = recall_score(y_test,y_pred)
    return f1, precision, recall