def isEven(value):
    buf = str(value)[-1]
    if buf == "0" or buf == "2" or buf == "4" or buf == "6" or buf == "8":
        return True
    else:
        return False
