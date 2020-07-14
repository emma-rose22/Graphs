stuff = {
  "cat": "bob",
  "dog": 23,
  19: 18,
  90: "fish"
}

#write a function that adds up numerical values in dict

# iterate through the keys
# if they are an int, add them to a list
# sum list and return it

def return_sum(stuff):
    to_add = []
    for i in stuff.values():
        if type(i) == int:
            to_add.append(i)

    return sum(to_add)

print(return_sum(stuff))
