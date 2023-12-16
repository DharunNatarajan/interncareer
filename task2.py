import numpy as np;
import pandas as pd;
import matplotlib.pyplot as pt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
iris = load_iris()
x = iris.data
y = iris.target
print(x)
print(y)
np.mean(x)
from scipy.stats import norm
def histogram(name,data):
    mean = np.mean(data)
    sd = np.std(data)
    x_axis = np.linspace(min(data), max(data),100)
    pt.plot(x_axis,norm.pdf(x_axis, mean, sd), color="Pink", label="Distributed in normal")
    pt.xlabel(f'{name}')
    pt.ylabel('density')
    pt.title(f'Normal Distribution - {name}')
    pt.legend()
    pt.show()
    pt.hist(data, bins = 20, density=True, alpha=0.6,color='red', label = "Histogram")
    pt.xlabel(f'{name}')
    pt.ylabel('density')
    pt.title(f'Histogram - {name}')
    pt.legend()
    pt.show()   
sep_len = np.random.normal(5, 0.5, 150)
sep_wid = np.random.normal(3, 0.3, 150)
pet_len = np.random.normal(4, 0.8, 150)
pet_wid = np.random.normal(1.5, 0.2, 150)
histogram("Sepal Length",sep_len)
histogram("Sepal Width",sep_wid)
histogram("Petal Length",pet_len)
histogram("Petal Width",pet_wid)


