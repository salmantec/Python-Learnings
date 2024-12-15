## Note: We can use mypy to enforce it, but here used decor to enforce it

def type_check(*expected_types):
    def decorator(func):
        def wrapper(*args, **kwargs):
                for arg, exp_type in zip(args, expected_types):
                    if not isinstance(arg, exp_type):
                        raise TypeError(f"Expected {exp_type} but got {type(arg)}")
                return func(*args, **kwargs)
        return wrapper
    return decorator


@type_check(int, int)
def add(a, b):
    return a+b

# print(add("10", "hello")) 
# print(add(10, "hello"))  
print(add(10, 20)) 


# def add(a: int, b: int):
#     return a + b

# print(add("10", "Hello"))