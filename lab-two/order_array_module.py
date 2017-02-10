def create_order_array():
    array = []
    for i in range(29):
        array.append(i)

    f = open("worst_case.dat", "w")
    for j in array:
        f.write("%s\n" %j)
        
if __name__ == '__main__':
    create_order_array()
    
    
