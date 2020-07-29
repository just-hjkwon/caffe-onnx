import src.c2oObject as Node
##--------------------------------------------------relu层------------------------------------------------------------##
#计算输出维度
def getSigmoidOutShape(input_shape):
    #获取output_shape
    output_shape = input_shape
    return output_shape
#构建节点
def createSigmoid(layer,nodename,inname,outname,input_shape):
    output_shape = getSigmoidOutShape(input_shape)
    node = Node.c2oNode(layer, nodename, "Sigmoid", inname, outname, input_shape, output_shape)

    print(nodename, "节点构建完成")
    return node
