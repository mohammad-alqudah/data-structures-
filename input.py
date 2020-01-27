import xlrd

from functions import findInVertexList


def carsNumber():
    while True:
        try:
            while True:
                carsNumber = int(input("Enter Number of cars in Amman : "))
                if carsNumber > 0:
                    return carsNumber
                else:
                    print("The number of cars cannot be less than zero")
            break
        except:
            print("This is a string")
def readFromExcel():


    loc = (r"C:\Users\mohammad alqudah\PycharmProjects\untitled7\Book1.xlsx")
    Arr=[]
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    sheet.cell_value(0, 0)

    for i in range(sheet.nrows):
	    Arr.append([])
	    Arr[i].append(sheet.cell_value(i, 0))
	    Arr[i].append(sheet.cell_value(i, 1))
	    Arr[i].append(sheet.cell_value(i, 2))
	    Arr[i].append(sheet.cell_value(i, 3))
	    Arr[i].append(sheet.cell_value(i, 4))
    Arr.remove(Arr[0])

    return (Arr)





def selectPoint(vertexList):
    while True:
        Point = str(input("Enter starting point : "))
        Point = findInVertexList(vertexList, Point)
        if Point >= 0:
            return Point
        else:
            print("The entered letter must be from one of the following letter",vertexList)



'''
def fromAndToWhere(vertexList):


    
    startPoint = str(input("Enter starting point : "))
    startPoint = findInVertexList(vertexList, startPoint)
    endPoint = str(input("Enter starting point : "))
    endPoint = findInVertexList(vertexList, endPoint)

    return startPoint, endPoint
'''