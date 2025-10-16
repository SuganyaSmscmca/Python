class MultipleFunctions():    
    def Subfields():
        print("Sub-fields in AI are:")
        subfields_name = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        for field in subfields_name:
            print(field)
    def oddEven():
        num=int(input("Enter a number:"))
        if ((num % 2) == 0):
            print(num," is Even number")        
        else:
            print(num," is Odd number")
    def Elegible():
        sex=input("Your Gender : ")
        age=int(input("Your Age : "))
        if(sex == 'female' and age<18):
            print("Not Eligible")
        elif(sex == 'female' and age>=18):
            print("Eligible")
        elif(sex == 'male' and age<21):
            print("Not Eligible")
        elif(sex == 'male' and age>21):
            print("Eligible")
        else:
            print("Invalid Input")
    def percentage():
        sub1=int(input("Subject1 = "))
        sub2=int(input("Subject2 = "))
        sub3=int(input("Subject3 = "))
        sub4=int(input("Subject4 = "))
        sub5=int(input("Subject5 = "))
        total = sub1+sub2+sub3+sub4+sub5
        percentage = (total / 500) *100
        print("Total:", total)
        print("Percentage:", percentage)
    def triangle():
        h=int(input("Height: "))
        b=int(input("Breadth: "))
        area=(h * b) / 2
        print("Area of Triangle: ",area)
        h1=int(input("Height1: "))
        h2=int(input("Height2: "))
        b1=int(input("Breadth: "))
        perimeter = h1+h2+b1
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle ",perimeter)