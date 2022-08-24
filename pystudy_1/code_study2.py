def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)


def print_n_times(n, *value):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "프로그래밍")

def print_n_times(value, n=2):
    for i in range(n):
        for value in values:
            print(values)

print_n_times("안녕하세요")

def print_n_times(*value,n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요", "즐거운", "프로그래밍", n=3)

def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")

return_test()

def return_test():
    return 100

value = return_test()
print(value)

def return_test():
    return

value = return_test()
print(value)