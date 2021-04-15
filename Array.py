# Array Operations in 1 Program

def maxelement(arr) :
    max = arr[0]
    i = 0
    n = len(arr)
    for i in range(n):
        if arr[i] > max :
            max = arr[i]
    return max

def addelement(arr) :
    pos = input("\nEnter position where you want to add : ")
    element = input("\nEnter Element :")
    arr.insert(int(pos),int(element))

    print("\n\nElement Added!!\n\nThe Array is : ")
    print(arr)
    print("\n\n")



def main() :
    arr = []
    while 1 == 1 :
        print("Menu : \n")
        print("1. Add Element in the Array")
        print("2. Delete Element in the Array")
        print("3. Maximum Element in the Array")
        print("4. Minimum Element in the Array")
        print("5. Display Sorted Array")
        print("4. Exit")
        case_var = input("Enter your choice : ")
        if case_var == '1':
            addelement(arr)
        elif case_var == '2':
            delelement()
        elif case_var == '3' :
            maxelement()
        elif case_var == '4' :
            break
        else :
            print ("\n\n\n Wrong Input!! Try Again.\n\n")

if __name__ == '__main__' :
    main()

        

        