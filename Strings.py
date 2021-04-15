def strmatch(t1, t2):
    if len(t1)==len(t2):
        print("Strings are equal in length.")

    if t1[0]==t2[0]:
        print("\nBoth strings have equal 1st character.")

    if t1[-1]==t2[-1]:
        print("\nBoth strings have equal last character.")

def main():
    text1 = input ("Enter a string: ")
    text2 = input ("Enter a string: ")
    strmatch(text1,text2)

if __name__ == "__main__":
    main()