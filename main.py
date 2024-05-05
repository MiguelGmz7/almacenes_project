from sklearn import datasets

# for dataset in dir(datasets):
#     print(dataset)

iris = datasets.load_iris()
iris.keys()
print(iris.DESCR)