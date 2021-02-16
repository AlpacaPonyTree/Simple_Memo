def string_to_list(str):
    list = [""]
    j = 0
    i = 0
    while i < len(str):
        if str[i] != ",":
            list[j] += str[i]
        else:
            j += 1
            list.append("")
        i += 1
    list.pop(j)
    return list
