import random
import time

## With Decor

def retry(retries=3, exception=Exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    attempts += 1
                    print(f"Failed ({attempts} / {retries})")
            raise exception
        return wrapper
    return decorator
     

@retry(retries=5, exception=ValueError)
# Lets say we have an API call which may throw an error, but sometimes it may work. In that case, we want to retry.
def error_prone_function():
    if random.random() < 0.9:
        raise ValueError("Error!")
    else:
        print("Success")



error_prone_function()



# ## With Decor (with delay)

# def retry(retries=3, exception=Exception, delay=2):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             attempts = 0
#             while attempts < retries:
#                 try:
#                     return func(*args, **kwargs)
#                 except exception as e:
#                     attempts += 1
#                     print(f"Failed ({attempts} / {retries})")
#                     time.sleep(delay)
#             raise exception
#         return wrapper
#     return decorator
     

# @retry(retries=5, exception=ValueError, delay=2)
# # Lets say we have an API call which may throw an error, but sometimes it may work. In that case, we want to retry.
# def error_prone_function():
#     if random.random() < 0.9:
#         raise ValueError("Error!")
#     else:
#         print("Success")



# error_prone_function()




## (w/o decor) One way to solve this retry - by using try except

# while True:
#     try:
#         error_prone_function()
#     except ValueError as e:
#         time.sleep(1) # Do the API call again