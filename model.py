import pandas as pd 
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle
import numpy


def train_and_save_model():
    data = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv')
    X = data.drop(columns=["medv"])
    y = data['medv']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)


    with open("model.pkl", "wb") as file:
        pickle.dump(model, file)

    print('pickle file saved. ')

if __name__ == "__main__":
    train_and_save_model()
    