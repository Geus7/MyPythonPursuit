def is_happy(n):
    def calculate_square_sum(num):
        sum_of_squares = 0
        while num > 0:
            digit = num % 10
            sum_of_squares += digit ** 2
            num //= 10
        return sum_of_squares

    seen_numbers = set()

    while n != 1 and n not in seen_numbers:
        seen_numbers.add(n)
        n = calculate_square_sum(n)

    return n == 1
n=int(input("Enter the number: "))
result = is_happy(n)
print(result)  
