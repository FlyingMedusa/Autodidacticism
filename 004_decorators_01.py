def my_decorator(target_function):
    def function_wrapper():
        return "Gandalf is such a " + target_function() + " wizard!"
    return function_wrapper

@my_decorator
def target_function():
    return "marvelous"

print(target_function())