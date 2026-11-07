from stack import Stack

def main():
    stack = Stack()

    stack.push(-2)
    stack.push(0)
    stack.push(-3)

    current_min_value = stack.get_min()
    print(current_min_value == -3)

    stack.pop()

    current_top = stack.top()
    print(current_top == 0)

    current_min_value = stack.get_min()
    print(current_min_value == -2)


if __name__ == "main":
    main()