def cough_dec(func):
    def func_wrapper():
        print('cough')
        func()
        print('cough')
    return func_wrapper

    
@cough_dec
def question():
    print('what is your name?')

question()