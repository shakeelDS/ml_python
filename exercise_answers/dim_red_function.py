from sklearn.decomposition import PCA 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score


def PCA_train_predict_score(X, y, k, random_state=42):
    """
    Function to perform PCA and generate model to check performance of given k components.
    
    Args:
    X (np.array (n,p)): Feature data
    y (np.array (n,)): Target data
    k (int): number of components for PCA to return
    random_state (int): random seed for train_test_split
    
    Returns:
    score (num): f1_score result of model trained.
    """
    # Split the data
    X_train, X_test, y_train, y_test = train_test_split(X, 
                                                        y, 
                                                        test_size=0.33, 
                                                        random_state=random_state)
    # Fit the PCA model
    pca = PCA(n_components=k).fit(X_train)
    
    # Our test data needs to be PCA'd on the original PCA model fit
    X_train = pca.transform(X_train)
    X_test = pca.transform(X_test)
    
    # Train the model 
    model = LogisticRegression().fit(X_train, y_train)
    
    # Generate predictions and score the predictions
    y_pred = model.predict(X_test)
    score = f1_score(y_test, y_pred)
    
    return score
