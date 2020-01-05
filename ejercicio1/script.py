def get_greatest(str_val, length):
    lst = []
    for i in range(len(str_val)-length+1):
        lst.append(int(str_val[i:i+length]))
    return max(lst)
