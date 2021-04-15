import math

def cube_sum(n) :
    i = 1
    sum = 0 
    for i in range(int(n)+1) :
        sum = sum + math.pow(i,3)
    
    return sum


def main() :
    range_var = input("Enter range : ")
    print("Cube sum of the series is :" + str(cube_sum(range_var)))


if __name__ == '__main__' :
    main()

