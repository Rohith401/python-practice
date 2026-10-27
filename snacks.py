fav={"navadeep":"chips","charan":"biscuits"}
print(fav["navadeep"])
fav["rohith"]="chocolate"
print(fav["rohith"])
who=input("Whose snacks?")
if who in fav:
    print(fav[who])
else:
    print("Name not found")
for name in fav:
    print(name,"likes",fav[name])
