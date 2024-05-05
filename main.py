
# # for dataset in dir(datasets):
# #     print(dataset)

# iris = datasets.load_iris()
# iris.keys()
# print(iris.DESCR)

# importamos pandas para poder leer el dataset
import pandas as pd
file_path = "BankOfAmericaCredits.csv"
df = pd.read_csv(file_path)

# definimos una variable "target" (x es el resto de las columnas, "y" la variable que queremos conocer)
target = "Approved"
x = df.drop(target, axis=1)
y = df[target]

# seleccionamos nuestros conjuntos de entrenamiento y prueba 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# creamos un algoritmo
from sklearn.naive_bayes import GaussianNB
method = GaussianNB()


method.fit(x_train,y_train)

#predecimos las clases de estos datos
y_pred = method.predict(x_test)

from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(y_test,y_pred)
print(matriz)



