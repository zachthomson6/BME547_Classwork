def fibinnaci(a, b, fib_list):
    next_number = a + b
    fib_list.append(next_number)
    count = 0
    if next_number < 10:
        fibinnaci(b, next_number, fib_list)
        count += 1
    else:
        print("sequence ending")
        return fib_list


def main():
    fib_list = []
    fib_list = fibinnaci(0, 1, fib_list)
    print(fib_list)


if __name__ == '__main__':
    main()