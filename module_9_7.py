def is_prime(funhin):
    def wrapper(*args, **kwargs):
        k = 0
        result = funhin(*args, **kwargs)
        for i  in range(2, result-1):
          
            if result % i == 0:
                 k = 0
                 break
            else: 
                k = 1

        if k != 0:
            return f'Простое \n{result}'
        else:
            return f'Состовное \n{result}'
    return wrapper
@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)