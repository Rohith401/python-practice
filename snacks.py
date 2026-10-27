fav={"navadeep":"chips","charan":"biscuits"}
fav["vishnu"]="cake"
fav["vishnu"]="samosa"
print(fav["navadeep"])
fav["rohith"]="chocolate"
print(fav["rohith"])
who=input("Whose snacks?")
if who in fav:
    print(fav[who])
else:
    print("Name not found")
new_name=input("New name?")
new_snack=input("Their snack?")
fav[new_name]=new_snack
for name in fav:
    print(name,"likes",fav[name])
