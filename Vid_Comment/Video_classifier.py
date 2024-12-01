import pandas as pd
import numpy
from sklearn.linear_model import  LinearRegression, LogisticRegression

def content_classifier(datas):
    df = pd.DataFrame(datas)
    print(df)