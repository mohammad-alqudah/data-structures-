from Vertex import Vertex, Edge


def removeDuplicate(duplicate):
    final_list = []
    for row in duplicate:
        if row[0] not in final_list:
            final_list.append(row[0])
    return final_list

def findInList(list,vertex):
    for i in range(len(list)):
        if list[i].name==vertex:
            return i



def dataProcessing(Vertexlist,list,Matrix):
    count = 0
    for i in Vertexlist:
        list.append(Vertex(i))

    for row in Matrix:
        VertexTo=findInList(list,row[1])
        if row[0]==list[count].name:
            list[count].adjacenciesList.append(Edge(row[2],list[count],list[VertexTo]))

        else:
            count=count+1
            list[count].adjacenciesList.append(Edge(row[2], list[count], list[VertexTo]))

def findInVertexList(list,Point):

    for i in range(len(list)):
        if str(list[i]) == Point:
            return i

    return -1
