dict1 = {"fname":"heidir","lname":"shah"}

dict2 = {
    "fname":"mohamad", "lname":"salah"
}

detail = {
    "person1":{
        "fname":"ali",
        "lname":"bakar"
    },

    "person2":{
        "fname":"abu",
        "lname":"talib"
    }
}

print(dict1)
print(dict1["fname"])
print(dict2["lname"])
print(detail["person1"])
print(detail["person2"]["fname"])

detail["person1"]["fname"] = "karim"
print(detail["person1"]["fname"])

del dict2["fname"]                      #delete content
print(dict2)

dict2["firstname"] = "ahmad"
dict2.update({"middlename":"nabil"})
print(dict2)

print(dict1)
dict1["fname"]="mohdheidir"
print(dict1)