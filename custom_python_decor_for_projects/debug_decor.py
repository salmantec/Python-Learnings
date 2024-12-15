def debug(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args {args} and kwargs {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result was {result}")
        return result    
    return wrapper

@debug
def add(a, b):
    return a + b

print(add(10, 20))