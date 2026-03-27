choices_list = ["a", "b", "c"]

def join_or(my_list, connector=", ", last_connector="or"):
    if len(my_list) == 0:
        return ""
    if len(my_list) == 1:
        return str(my_list[0])
    if len(my_list) == 2:
        return f"{my_list[0]} {last_connector} {my_list[1]}"

    beginning = connector.join(my_list[:-1])
    last = f" {my_list[-1]}"
    return  beginning + connector + last_connector + last

choices_str = join_or(choices_list)
print(f"Choose a square ({choices_str}): ")