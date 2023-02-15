def my_function():
    email = "zach.thomson@duke.edu"
    checker = "@" in email
    try:
        answer = checker[1]
    except TypeError:
        answer = checker
    return answer


def main():
    my_function()
    
    
if __name__ == "__main__":
    main()
