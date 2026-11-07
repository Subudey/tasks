from stack import Stack
from underground_system import UndergroundSystem


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


    system = UndergroundSystem()
    system.check_in(1, "a", 2)
    system.check_in(2, "a", 3)
    system.check_out(1, "b", 5)
    system.check_out(2, "b", 10)

    print(system.get_average_time('a', 'b'))



if __name__ == "__main__":
    main()