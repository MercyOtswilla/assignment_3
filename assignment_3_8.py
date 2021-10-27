def main():
    total = 0
    for i in range(5):
        numbers = int(input("Enter numbers: "))
        total = total + numbers
        average = (total / 5)
        print("The sum and average are", total,average, "respectively.")

        
main()
