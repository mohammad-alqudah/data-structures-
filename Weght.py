def Weght(Matrix,numberOfCar):

    weght=[]
    for row in Matrix:
        percentage =float(row[4]/100)
        threshold=(int(row[3]))
        distance=int(row[2])

        if  numberOfCar*percentage > threshold:
            Weght=(numberOfCar*percentage-threshold)/threshold*4*distance+distance
            weght.append([row[0],row[1],Weght])
        else: weght.append([row[0],row[1],distance])

    return weght

