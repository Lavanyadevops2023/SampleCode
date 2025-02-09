#polindrome or not
string= input("Enter the string:")
if(string ==string[::-1]):
    print("given string is polindrome")
else:
    print("given string is not a polindrome")

#seperate string and integer
number=[]
name=[]
List1=['asdf',232,'gfhgh',65676,'tytu']
for i in List1:
    if type(i)==int:
        number.append(i)
    if type(i)==str:
        name.append(i)
print("seperation of numbers are:",number,"separation of name is:",name)



