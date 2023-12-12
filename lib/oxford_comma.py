def oxford_comma(items):
    num_items = len(items)
    if num_items == 0:
        return ""
    elif num_items == 1:
        return items[0]
    elif num_items == 2:
        return " and ".join(items)
    else:
        return ", ".join(items[:-1]) + ", and " + items[-1]
