fav={"ramu":"biryani","sita":"dosa"}
print(fav["sita"])
fav["rohith"]="idli"
print(fav["rohith"])
who=input("Whose food?")
if who in fav:
    print(fav[who])
else:
    print("Name not found")
for name in fav:
    print(name,"likes",fav[name])
