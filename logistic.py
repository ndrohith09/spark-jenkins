# Save Model Using joblib
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
test_size = 0.36
# test_size = 0.33
seed = 7
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)

# Fit the model on training set
print("Creating Logistic Regression Model ..")
model = LogisticRegression()
print("Training Model ..")
model.fit(X_train, Y_train)
# save the model to disk
print("Saving Model ..")
filename = 'logistic.sav'
joblib.dump(model, filename)
print("Model Saved ..")

# load the model from disk
print("Loading Saved Model ..")
loaded_model = joblib.load(filename)
result = loaded_model.score(X_test, Y_test)
print("==================================================")
print("\n Score = " , result)