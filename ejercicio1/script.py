def get_greatest(str_val, length):
    greatest = None
    for i in range(len(str_val)-length+1):
        greatest = max(greatest or 0, int(str_val[i:i+length]))
    return greatest
