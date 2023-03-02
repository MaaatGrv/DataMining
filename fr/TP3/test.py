from sklearn import tree
import graphviz
import pydotplus
from IPython.display import Image, display

data = [[0, 0], [1, 1], [1, 0]]
result = [1, 0, 1]
dtc = tree.DecisionTreeClassifier()
dtc = dtc.fit(data, result)

dot_data = tree.export_graphviz(
    dtc,
    out_file=None,
    feature_names=["column1", "column2"],
    filled=True,
    rounded=True,
    class_names=["class1", "class2"],
)
graph = graphviz.Source(dot_data)
pydot_graph = pydotplus.graph_from_dot_data(dot_data)
img = Image(pydot_graph.create_png())
display(img)