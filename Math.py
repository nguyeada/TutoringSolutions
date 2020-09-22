def GCF():
    i = 0
    GCF_input=input("Please enter a list of numbers separated by commas: ")
    numbers = []
    for word in GCF_input.split(","):
        if word.isdigit():
            numbers.append(int(word))
    array = []
    max = 1

    for x in numbers:
        factors = set()
        for y in range(1, x+1):
            if x % y == 0:
                factors.add(y)
        array.append(factors)
    for x in array[0]:
        for y in range(1,len(array)):
            if x in array[y]:
                if x>max:
                    max=x
    print("The GCF value is: " + str(x))


def LCM():
    i=0
    LCM_input= input("Please enter a list of numbers separated by commas: ")
    numbers =[]
    for word in LCM_input.split(","):
        if word.isdigit():
            numbers.append(int(word))
    array = []
    numbers.sort(reverse=True)
    print(numbers)
    max_LCM = 1
    for x in numbers:
        max_LCM *=x
    i=0

    for x in numbers:
        num =1
        multiples = set()
        i=0
        while num< max_LCM:
            i+=1
            num= x*i
            multiples.add(num)
        array.append(multiples)
    for x in array[0]:
        is_in_all = True
        for y in range(1,len(array)):
            if x not in array[y]:
                is_in_all = False
                break
        if is_in_all and x<max_LCM:
            max_LCM=x
    print("The LCM value is: " + str(max_LCM))




def Mean():
    mean_input = input("Please enter a list of numbers separated by commas: ")
    numbers = []
    for word in mean_input.split(","):
        if word.isdigit():
            numbers.append(int(word))
    # print(numbers)
    mean = 0
    for x in range(len(numbers)):
        mean +=int(numbers[x])
    mean = (mean/(len(numbers)))
    print("The mean is: "+ str(mean))







print("Welcome! Let's check your answers. When you're finished type exit to end program")
category = ""
while category != "exit":
    print("1. GCF\n2. LCM\n3. Mean\n4. Median\n5. Mode\n6. Decimals\n7. Fractions\n8. Area\n9. Surface Area")
    category = input("Please pick a Category: ")
    if category== "3" or "Mean":
        Mean()








