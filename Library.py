class Library:

    def __init__(self,booklist,name):
        self.Booklist = booklist
        self.name = name
        self.lendbook={}

    def BookAdd(self , newbook):
        self.Booklist.append(newbook)


    def lendingBook(self,book , user):
        if book  in self.Booklist:
            if book not in self.lendbook.keys():
                self.lendbook.update({book:user})
                print("book ",book ," is lended You")
            else:
                print("sorry some one as got this book")


        else:
            print("We dont have this Book")
        

    def returnBook(self,book):
        if book  in self.lendbook.keys():
            del self.lendbook[book]
            print("Book ",book," is returned")
        else:
            print("Sorry this book dooesnt belongs to out library")

    def show(self):
        return ("The {}  library as this {} Books".format(self.name , self.Booklist) )

if __name__ == "__main__":

    kamal = Library(['c++','java','python','machine Learning',"data science"],"codekamli")
    
    chance = 3
    while chance != 0:
    
        print("Welcome to " , kamal.name , "Library") 
        print("Enter 1 to Show the List of Books")
        print("Enter 2 to Get the Books")
        print("Enter 3 to Return Book")
        print("Enter 4 to Exit")


        choice = int(input("Enter Your Choice "))

        if choice is 1:
            print(kamal.show())


        elif choice is 2:
            Bookname = input("Enter the Book name ")
            username = input("Enter Yout name ")

            kamal.lendingBook(Bookname,username)


        elif choice is 3:
            book = input("Enter the Book")
            kamal.returnBook(book)

        elif choice is 4:
            print("Thank You Visit Again")
            break

        else:
            print("Invalid Choice")


        print("Enter C to Continue or Enter Q to quit")

        Wish = input("Enter Your Wish")

        if Wish is 'c' and Wish is not 'q':
            chance-=1
            continue
        else:
            print("Thank You Visit Again")
            break

    if chance == 0:
        print("Your Credentials to Acces",kamal.name," Library is Over just Login again , ""Thankyou"" ")
    else:
        pass
            
    
    




   
