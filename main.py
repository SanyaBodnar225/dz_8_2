import time

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

# Приклад іншої функції, яку ви хочете виміряти
def example_function(x, y):
    return x + y

# Тести для перевірки працездатності
def run_tests():
    # Тест 1
    result, execution_time = measure_time(example_function, 3, 4)
    print(f"Result: {result}, Execution Time: {execution_time} seconds")

    # Тест 2 (можете додати більше тестів)
    result, execution_time = measure_time(example_function, 5, 10)
    print(f"Result: {result}, Execution Time: {execution_time} seconds")

if __name__ == "__main__":
    run_tests()
