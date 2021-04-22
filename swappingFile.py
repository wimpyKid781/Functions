def swapFileData():
    file1 = input("Enter file name: ")
    file2 = input("Enter other file name: ")
    with open(file1, "r") as a:
        data_a = a.read
    
  

    with open(file2,"r") as b:
        data_b = b.read


    with open(file1,"w") as a:
        data_a = b.write
        print(data_a) 

        
    with open(file2,"w") as b:
        data_b = a.write
        print(data_b)

 

   

swapFileData()
    

