marks = {
    "Shrasti": 80,
    "Kamini": 90,
    "Aditya": 89
}

marks.update({"Aditya": 80})
marks.update({"Shrasti": 89})
print(marks.get("Shrasti"))
#print(marks, type(marks)) 
#print(marks.keys())
#print(marks.items())
#print(marks.values())