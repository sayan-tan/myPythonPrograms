def months(name, days):
    print("The " + str(name) + " month has " + str(days) + " days.")

def main() :
    m_name = input("Enter name of the month : ")
    days = input("Enter number of days : ")
    months(m_name, days)

if __name__ == '__main__' :
    main()