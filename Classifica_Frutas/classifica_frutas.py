from sklearn import tree

# x = [peso(gramas), casca]
# 1 = Lisa, 0 = Rugosa
# 5 = Maçã, 10 = Laranja
x = [[140, 1], [130, 1], [158, 0], [178, 0]]
y = [5, 5, 10, 10]

clf = tree.DecisionTreeClassifier()# Instancia uma árvore para classificação
clf = clf.fit(x, y)# Treinando o computador

print (clf.predict([[200, 0]]))# Classifica uma nova fruta


