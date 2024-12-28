from sklearn import datasets 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score 
# Load Iris dataset 
iris = datasets.load_iris() 
X = iris.data 
y = iris.target 
# Split the dataset 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) 
# Build the model 
model = RandomForestClassifier() 
model.fit(X_train, y_train) 
# Make predictions 
y_pred = model.predict(X_test) 
# Evaluate the model 
accuracy = accuracy_score(y_test, y_pred) 
print(f"Accuracy of the model: {accuracy:.2f}")