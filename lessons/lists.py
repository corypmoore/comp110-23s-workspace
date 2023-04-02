"""Practice with lists."""

grocery_list: list[str] = list()
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")
grocery_list[1] = "cereal"
grocery_list.pop(2)
print(grocery_list)

def dup(xs: list[str]):
    start_len: int = len(xs)
    i: int = 0
    while i <= start_len - 1:
        xs.append(xs[i])
        i += 1
        
groceries: list[str] = ["apples", "eggs"]
print(dup(groceries))
print(groceries)