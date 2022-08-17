from decorator import decorator

cook_book = {}
with open("recipes.txt", "r", encoding = "utf-8") as f:
    for line in f:
        dish_name = line.strip()
        amount = int(f.readline().strip())
        res = []
        for i in range(amount):
            ingreds = {}
            ingr = f.readline().split("|")
            ingreds["ingredient_name"] = ingr[0].strip()
            ingreds["quantity"] = int(ingr[1])
            ingreds["measure"] = ingr[2].strip()
            res.append(ingreds)
        f.readline()
        cook_book[dish_name] = res

@decorator
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in cook_book.keys():
        if dish in dishes:
            for i in cook_book[dish]:
                result = {}
                result["measure"] = i["measure"]
                result["quantity"] = i["quantity"] * person_count
                shop_list[i["ingredient_name"]] = result
                if i["ingredient_name"] in shop_list:
                    result["quantity"] += result["quantity"]
    return shop_list

if __name__ == '__main__':
    get_shop_list_by_dishes(["Запеченный картофель", "Омлет"], 3)