# Read about print()


def print_hello_world():
    return("Hello World")
    pass


def sum(first, second):
    return(first+second)

# Read if-else construct


def get_largest_number(first, second):
    return max(first,second)

# Read nested if-else construct


def get_largest_of_three(first, second, third):
    k=[first, second, third]
    return max(k)

# Go through arrays in python using for loop


def print_array(num):
    a=[]
    for i in range(0,num):    
        a.append(i)
    return a
    


def get_sum_of_array(array):
    sum=0
    for i in array:
        sum=sum+i
    return sum
    pass


def isPrime(number):
    if number > 1:
        for i in range(2, int(number//2)+1):
            if (number % i) == 0:
                return("not prime")
                break
        else:
            return("prime")
    else:
        return("not prime")


# Say, first = 5 and second = 10, this function should print "5 6 7 8 9 10"


def get_array_of_range_of_numbers(first,  second):
    a=[]
    for i in range(first,second+1):    
        a.append(i)
    return a
    pass


def get_factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f


def get_factorial_without_loop(n):
    if n<0:
        return("enter positive n")
    elif n==0 or n==1:
        return 1
    else:
        return(n*get_factorial_without_loop(n-1))

    pass

# 1234 should give 4321


def reverse_digits(n):
    k=(str(n)[::-1])
    return int(k)
    pass

# In between 1 to 10, the prime numbers are 1, 2, 3, 5, 7


def prime_numbers_in_range(lowerLimit, upperLimit):
    a=[]
    for num in range(lowerLimit, upperLimit + 1):
        flag=True
        if num > 1:
            for i in range(2, num):
                if (num % i)== 0:
                    flag=False
                    break
            if flag:
                a.append(num)
        
    return a
    pass


def find_number_of_occurences(array, number):
    count = 0
    for i in array:
        if (i == number):
            count = count + 1
    return count


def find_first_occurences(array, number):
     for i in range(len(array)):
        if (array[i] == number):
            return i


def print_rhombus(num):
    a=""
    for i in range(0, num):
        for j in range(1, i+1):
            a+=" "
        for j in range(0, num):
            a+="*"
        a+="\n"
    return a.strip()




def number_to_word(n):
    arr = ['zero','one','two','three','four','five','six','seven','eight','nine']
    if(n==0):
        return ""
    else:
        small_ans = arr[n%10]
        ans = number_to_word(int(n/10)) + small_ans + " "
    return ans


def print_triangle_pointing_right(size):
    ans=""
    for i in range(0,size+1):
        for j in range(0+i):
            ans+="#"
        ans+="\n"
    return ans.strip()