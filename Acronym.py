def acronym(str):
    acr = str.split()
    new = ""

    for i in range(len(acr)):
        str = acr[i]
        new = new + (str[0].upper())
    return new

str = "Universal Serial Bus"
print(acronym(str))
