def acronym(str):
    strnew = str.split()
    result = ""

    for word in strnew:
        result += word[0].upper()
    
    return result


str = input("Enter a String: ")
print(acronym(str))
