from Algorthem import Algorithm
from Weght import Weght
from functions import removeDuplicate,  dataProcessing
from input import readFromExcel,  selectPoint
from input import carsNumber



StreetInformation =readFromExcel()
carsNumber=carsNumber()
Matrix =Weght(StreetInformation,carsNumber)
Vertexlist=removeDuplicate(Matrix)
startPoint=selectPoint(Vertexlist)
endPoint=selectPoint(Vertexlist)

list=[]
edge=[]
node=[]

dataProcessing(Vertexlist,list,Matrix)
algoithm = Algorithm()
algoithm.calculateShortestPath(list[startPoint])
algoithm.getShortestPathTo(list[endPoint])


