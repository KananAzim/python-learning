def print_doc():
        
        doc = open("workerlist.txt","a")
        h = doc.readlines()
        print(h)

def add_worker():
        
        d = open("workerlist.txt","a")
        g = d.write(input("Enter: "))
        print(g)

            
p = ["1.Print all workers","2.Add worker","3.Delete worker","4.Exit"]
for n in p:
        print(n, end= "\n")
print()


while True:
       

        

        k = int(input("Choice:"))
        if k==1:

                print_doc()
        elif k==2:
                add_worker()

            
                










        


        

        

