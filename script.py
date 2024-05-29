def my_split(mstr):
    ms = []
    string = ""
    for i in mstr:
        if i == " ":
            ms.append(string)
            string = ""
        else:
            string += i
    if string:
        ms.append(string)
    return ms

def my_upper(mstr):
    ms = ""
    for i in mstr:
        if "a" <= i <= "z":
            ms += chr(ord(i) - 32)
        else:
            ms += i
    return ms

def my_reverse(mstr):
    if type(mstr) == str:
        tmp = ""
        for i in mstr:
            tmp = i + tmp
        return tmp
    else:
        return "no string"

def main():
    mstr = "hello world"
    print(my_split(mstr))
    print(my_upper(mstr))
    print(my_reverse(mstr))

if __name__ == "__main__":
    main()
