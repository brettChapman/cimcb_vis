import networkx as nx
import numpy as np
from networkx.drawing.nx_agraph import pygraphviz_layout
import matplotlib.pyplot as plt
import copy
from .utils import *

import warnings
warnings.filterwarnings("ignore")

class plotNetwork:

    def __init__(self, g):

        self.__g = self.__checkData(copy.deepcopy(g))

        self.set_params()

    def __checkData(self, g):

        if not isinstance(g, nx.classes.graph.Graph):
            raise ValueError("A networkx graph was not entered. Please check your data.")

        return g

    def set_params(self, node_params, filter_params, imageFileName='networkPlot.jpg', saveImage=True, graphviz_prog='neato', figSize=(30,20)):

        self.__set_node_params(**node_params)

        self.__set_filter_params(**filter_params)

        imageFileName, saveImage, graphviz_prog, figSize = self.__paramCheck(imageFileName, saveImage, graphviz_prog, figSize)

        self.__imageFileName = imageFileName;
        self.__saveImage = saveImage;
        self.__graphviz_prog = graphviz_prog;
        self.__figSize = figSize;

    def __set_node_params(self, sizing_column='Pvalue', sizeScale='reverse_linear', size_range=(150,2000), alpha=0.5, addLabels=True, fontSize=15, keepSingletons=True):

        sizing_column, sizeScale, size_range, alpha, addLabels, fontSize, keepSingletons = self.__node_paramCheck(sizing_column, sizeScale, size_range, alpha, addLabels, fontSize, keepSingletons)

        self.__sizing_column = sizing_column;
        self.__sizeScale = sizeScale;
        self.__size_range = size_range;
        self.__alpha = alpha
        self.__addLabels = addLabels
        self.__fontSize = fontSize;
        self.__keepSingletons = keepSingletons;

    def __set_filter_params(self, column='Pvalue', threshold=0.01, operator='>', sign='both'):

        column, threshold, operator, sign = self.__filter_paramCheck(column, threshold, operator, sign)

        self.__filter_column = column;
        self.__filter_threshold = threshold;
        self.__operator = operator;
        self.__sign = sign;

    def __paramCheck(self, imageFileName, saveImage, graphviz_prog, figSize):

        if not isinstance(imageFileName, str):
                raise ValueError("Image file name is not valid. Choose a string value.")

        if not type(saveImage) == bool:
            raise ValueError("Save image is not valid. Choose either \"True\" or \"False\".")

        if graphviz_prog not in ["neato", "dot", "fdp", "sfdp", "twopi", "circo"]:
            raise ValueError("Graphviz layout program not valid. Choose either \"neato\", \"dot\", \"fdp\", \"sfdp\", \"twopi\" or \"circo\".")

        if not isinstance(figSize, tuple):
            raise ValueError("Figure size is not valid. Choose a tuple of length 2.")
        else:
            for length in figSize:
                if not isinstance(length, float):
                    if not isinstance(length, int):
                        raise ValueError("Figure size items not valid. Choose a float or integer value.")

        return imageFileName, saveImage, graphviz_prog, figSize

    def __node_paramCheck(self, sizing_column, sizeScale, size_range, alpha, addLabels, fontSize, keepSingletons):

        if sizing_column not in col_list:
            raise ValueError("Sizing column not valid. Choose one of {}.".format(', '.join(col_list)))
        else:
            for idx, node in enumerate(g.nodes()):
                try:
                    float(g.node[node][sizing_column])
                except ValueError:
                    raise ValueError(
                        "Sizing column contains invalid values. Choose a sizing column containing float or integer values.")

        if sizeScale.lower() not in ["linear", "reverse_linear", "log", "reverse_log", "square", "reverse_square", "area", "reverse_area", "volume", "reverse_volume"]:
            raise ValueError(
                "Size scale type not valid. Choose either \"linear\", \"reverse_linear\", \"log\", \"reverse_log\", \"square\", \"reverse_square\", \"area\", \"reverse_area\", \"volume\", \"reverse_volume\".")

        if not isinstance(size_range, tuple):
            raise ValueError("Size range is not valid. Choose a tuple of length 2.")
        else:
            for size in size_range:
                if not isinstance(size, float):
                    if not isinstance(size, int):
                        raise ValueError("Size items not valid. Choose a float or integer value.")

        if not isinstance(alpha, float):
            if not (alpha >= 0 and alpha <= 1):
                raise ValueError("Alpha value is not valid. Choose a float between 0 and 1.")

        if not type(addLabels) == bool:
            raise ValueError("Add labels is not valid. Choose either \"True\" or \"False\".")

        if not isinstance(fontSize, float):
            if not isinstance(fontSize, int):
                raise ValueError("Font size is not valid. Choose a float or integer value.")

        if not type(keepSingletons) == bool:
            raise ValueError("Keep singletons is not valid. Choose either \"True\" or \"False\".")

        return sizing_column, sizeScale, size_range, alpha, addLabels, fontSize, keepSingletons

    def __filter_paramCheck(self, column, threshold, operator, sign):

        g = self.__g
        col_list = list(g.nodes[0].keys())

        if column not in col_list:
            raise ValueError("Filter column not valid. Choose one of {}.".format(', '.join(col_list)))
        else:
            for idx, node in enumerate(g.nodes()):
                try:
                    float(g.node[node][column])
                except ValueError:
                    raise ValueError(
                        "Filter column contains invalid values. Choose a filter column containing float or integer values.")

        if not isinstance(threshold, float):
            if not isinstance(threshold, int):
                raise ValueError("Filter threshold is not valid. Choose a float or integer value.")
            elif threshold == 0:
                raise ValueError("Filter threshold should not be zero. Choose a value close to zero or above.")
        elif threshold == 0.0:
            raise ValueError("Filter threshold should not be zero. Choose a value close to zero or above.")

        if operator not in ["<", ">", "<=", ">="]:
            raise ValueError("Operator not valid. Choose either \"<\", \">\", \"<=\" or \">=\".")

        if sign.lower() not in ["pos", "neg", "both"]:
            raise ValueError("Sign not valid. Choose either \"pos\", \"neg\", or \"both\".")

        return column, threshold, operator, sign

    def run(self):

        g = self.__g

        plt.subplots(figsize=self.__figSize);

        #//edges = list(g.edges())
        edgeList = []
        for idx, (source, target) in enumerate(g.edges()):
            #//print(edge)
            #source = u
            #target = v
            weight = g.edges[source, target]['weight']

            if self.__sign == "pos":
                if weight < 0:
                    edgeList.append((source, target))
            elif self.__sign == "neg":
                if weight >= 0:
                    edgeList.append((source, target))

        g.remove_edges_from(edgeList)

        nodeList = []
        for idx, node in enumerate(g.nodes()):

            value = float(g.node[node][self.__filter_column])

            if value > float(self.__filter_threshold):
                nodeList.append(node)

        for node in nodeList:
            g.remove_node(node)

        if not self.__keepSingletons:
            edges = list(g.edges())
            edgeList = []
            for edge in edges:
                source = edge[0]
                target = edge[1]

                edgeList.append(source)
                edgeList.append(target)

            edgeNodes = np.unique(edgeList)

            singleNodes = list(set(edgeNodes).symmetric_difference(set(list(g.nodes()))))

            for node in singleNodes:
                g.remove_node(node)

        size_attr = np.array(list(nx.get_node_attributes(g, self.__sizing_column).values()))

        size = np.array([x for x in list(range_scale(size_attr, 1, 10))])

        if self.__sizeScale == 'linear':
            node_size = [x for x in list(range_scale(size, self.__size_range[0], self.__size_range[1]))]
        if self.__sizeScale == 'reverse_linear':
            size = np.divide(1, size)
            node_size = [x for x in list(range_scale(size, self.__size_range[0], self.__size_range[1]))]
        elif self.__sizeScale == 'log':
            size = np.log(size)
            node_size = [x for x in list(range_scale(size, self.__size_range[0], sellf.__size_range[1]))]
        elif self.__sizeScale == 'reverse_log':
            size = np.divide(1, size)
            size = np.log(size)
            node_size = [x for x in list(range_scale(size, self.__size_range[0], self.__size_range[1]))]
        elif self.__sizeScale == 'square':
            size = np.square(size)
            node_size = [x for x in list(range_scale(size, self.__size_range[0], self.__size_range[1]))]
        elif self.__sizeScale == 'reverse_square':
            size = np.divide(1, size)
            size = np.square(size)
            node_size = [x for x in list(range_scale(size, self.__size_range[0], self.__size_range[1]))]
        elif self.__sizeScale == 'area':
            #size = [np.square(x) for x in list(map(float, size))]
            size = np.square(size)
            size = [np.multiply(x, np.pi) for x in list(map(float, size))]
            node_size = [round(x) for x in list(map(int, range_scale(size, self.__size_range[0], self.__size_range[1])))]
        elif self.__sizeScale == 'reverse_area':
            size = np.divide(1, size)
            size = np.square(size)
            size = [np.multiply(x, np.pi) for x in list(map(float, size))]
            node_size = [round(x) for x in list(map(int, range_scale(size, self.__size_range[0], self.__size_range[1])))]
        elif self.__sizeScale == 'volume':
            size = [np.power(x, 3) for x in list(map(float, size))]
            size = [np.multiply(x, np.pi) for x in list(map(float, size))]
            size = [np.multiply(x, 4 / 3) for x in list(map(float, size))]
            node_size = [round(x) for x in list(map(int, range_scale(size, self.__size_range[0], self.__size_range[1])))]
        elif self.__sizeScale == 'reverse_volumn':
            size = np.divide(1, size)
            size = [np.power(x, 3) for x in list(map(float, size))]
            size = [np.multiply(x, np.pi) for x in list(map(float, size))]
            size = [np.multiply(x, 4 / 3) for x in list(map(float, size))]
            node_size = [round(x) for x in list(map(int, range_scale(size, self.__size_range[0], self.__size_range[1])))]

        pos = pygraphviz_layout(g, prog=self.__graphviz_prog)

        nx.draw(g, pos=pos, labels=dict(zip(g.nodes(), list(nx.get_node_attributes(g, 'Label').values()))), node_size=node_size, font_size=self.__fontSize, node_color=list(nx.get_node_attributes(g, 'Color').values()), alpha=self.__alpha, with_labels=self.__addLabels)

        if self.__saveImage:
            plt.savefig(self.__imageFileName, format="JPG");

        plt.show()