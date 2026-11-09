from main import addition, subtraction, multiplication, division


def test():
    # Addition
    assert addition(2, 3) == 5
    assert addition(-2, 3) == 1

    # Subtraction
    assert subtraction(5, 3) == 2
    assert subtraction(3, 5) == -2

    # Multiplication
    assert multiplication(3, 4) == 12
    assert multiplication(-2, 5) == -10

    # Division
    assert division(10, 2) == 5
    assert division(7, 2) == 3.5



if __name__ == "__main__":
    test()
    print("All tests passed!")