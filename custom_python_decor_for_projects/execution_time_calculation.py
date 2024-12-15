import time 


## With Decorator

def time_logger(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Time taken: {end-start:.4f}")
        return result
    return wrapper

@time_logger
def process_input(n):
    time.sleep(2)
    return n**2

print(process_input(5))

## W/O decorator:


# def process_input(n):
#     time.sleep(2)
#     return n**2

# start = time.perf_counter()
# process_input(2)
# end = time.perf_counter()

# print("Time taken:", end-start)
