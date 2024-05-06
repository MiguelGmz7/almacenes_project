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

# entrenamos el modelo
method.fit(x_train,y_train)


Ethnicity = ['asiatico', 'negro', 'latino', 'otro', 'blanco']
Industry = ['comunicacion','entretenimiento','agropecuario','educacion','energia','finanzas','salud','industrial','tecnologia','materiales',
            'bienes raices','investigacion','transporte','gobierno']
# gender = input("Ingresa tu genero: ")
# income = input("Ingresa tu ingreso mensual: ")
# creditscore = input("Ingresa tu puntaje de credito: ")
# bankcostumer = input("cliente: ")
# industria = input("industria: ")
# etnia = input("etnia ")
# trabajo = input("ingresa tus años trabajados ")
# credito = input("ya tenias un credito: ")
# empleado = input("eres empleado: ")
# deuda = input("deuda: ")
# licencia = input("licencia: ")
# edad = input("edad: ")
# ciudadano = input("eres ciudadano: ")

#Crear un diccionario con los datos
data = {
    'Gender': [1],
    'Income': [0],
    'CreditScore': [0],
    'BankCustomer': [0],
    'Industry': [1],
    'Ethnicity': [0.25],
    'YearsEmployed': [10.000],
    'PriorDefault': [1],
    'Employed': [0],
    'Debt': [2.250],
    'DriversLicense': [1],
    'Age': [40.92],
    'Citizen': [0]
}

#Crear el DataFrame
client = pd.DataFrame(data)
print(client)

pred = method.predict(client)
print(pred)

#predecimos las clases de estos datos
y_pred = method.predict(x_test)

if pred[0] == 1:
    print("es 1!!!!!!")
else:
    print("es 0!!!!!!")

from sklearn.metrics import confusion_matrix

matriz = confusion_matrix(y_test,y_pred)
print("Matriz de confunsion")
print(matriz)

# tenemos una precision del modelo
from sklearn.metrics import precision_score
pres = precision_score(y_test,y_pred)
print("precision del modelo")
print(pres)


