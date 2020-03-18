def swap_case(s):
    a = ""
    for i in s:
        if i.isUpper()==True:
            a+=(i.lower())
        else:
            a+=(i.upper())
    return a


if __name__ == '__main__':
    s = raw_input()
    result = swap_case(s)
    print result