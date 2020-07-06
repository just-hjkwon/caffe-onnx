import src.c2oObject as Node
##---------------------------------------------softmax层--------------------------------------------------------------##
#获取超参数
def getSoftmaxAttri(layer):
    ##轴
    axis = layer.softmax_param.axis
    #超参数字典
    dict = {"axis": axis}
    return dict
#计算输出维度
def getSoftmaxOutShape(input_shape):
    #计算输出维度output_shape
    output_shape = input_shape#与输入维度一样
    return output_shape
#构建节点
def createSoftmax(layer, nodename, inname, outname, input_shape, axis):
    output_shape = getSoftmaxOutShape(input_shape)
    #构建node
    node = Node.c2oNode(layer, nodename, "Softmax", inname, outname, input_shape, output_shape, dict)
    print(nodename, "节点构建完成")
    return node

def createExp(layer, nodename, inname, outname, input_shape):
    output_shape = input_shape
    #构建node
    node = Node.c2oNode(layer, nodename, "Exp", inname, outname, input_shape, output_shape)
    print(nodename, "节点构建完成")
    return node

def createReduceSum(layer, nodename, inname, outname, input_shape, axis, keep_dims=False):
    dict = {'axes': [axis], 'keepdims': (1 if keep_dims is True else 0)}

    output_shape = input_shape
    #构建node
    node = Node.c2oNode(layer, nodename, "ReduceSum", inname, outname, input_shape, output_shape, dict)
    print(nodename, "节点构建完成")
    return node    


def createDiv(layer, nodename, inname, outname, input_shape):
    output_shape = [input_shape[0]]
    #构建node
    node = Node.c2oNode(layer, nodename, "Div", inname, outname, input_shape, output_shape)
    print(nodename, "节点构建完成")
    return node    

def createTranspose(layer, nodename, inname, outname, input_shape, perm):
    dict = {'perm': perm}

    output_shape = []
    output_shape.append([])
    for i in range(len(input_shape[0])):
        output_shape[0].append(input_shape[0][perm[i]])
    
    node = Node.c2oNode(layer, nodename, "Transpose", inname, outname, input_shape, output_shape, dict)
    print(nodename, "节点构建完成")
    return node        
