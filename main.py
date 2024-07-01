calls = 0 
def count_calls (): #подсчитывающая вызовы остальных функций
    global calls
    calls = calls + 1

def string_info(string): #принимает аргумент - строку и возвращает кортеж
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search): #принимает два аргумента: строку и список, и возвращает True, False
    count_calls()
    for i in list_to_search:
        a = [i.lower() for i in list_to_search]

        return string.lower() in a

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycle', 'cyclic']))
print(calls)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
