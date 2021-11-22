from dataclasses import dataclass
from typing import List


@dataclass
class Result:
    a: int
    b: int
    q: int


# d = ax + by
def gcdExt(a: int, b: int) -> (int, int, int):
    """
    returns (gcd, s, t) where
    gcd is the gcd of a and b and
    g = s * a + t * b
    """

    # start by calculating the gcd of a and b
    # save the results in a list
    results: List[Result] = []
    q = 0

    # repeat until b = 0 (when b = 0 we have found the gcd)
    while b != 0:
        # a = b * q
        q = a // b  # q = a / b ( '//' means round down)

        # save results to the list
        results.append(Result(a, b, q))

        # calculate the new a and b
        # a = b
        # b = a % b ('%' means modulo)

        # make temporary copies because we need the old a and b
        # to calculate the new a and b
        a1, b1 = (b, a % b)
        a, b = (a1, b1)

    gcd = a

    # gcd = a * s1 + b * t1
    s, t = (1, 0)

    # start going backwards through our calculations
    results.reverse()
    for result in results:
        # calculate the new s and t
        # s = t
        # t = s - q * t

        # make temporary copies because we need the old s and t
        # to calculate the new s and t
        s1, t1 = (t, s - result.q * t)
        s, t = (s1, t1)

    return (gcd, s, t)


if __name__ == "__main__":
    numbers = [int(num) for num in input("enter two numbers: ").split(" ")]
    result = gcdExt(numbers[0], numbers[1])
    print(
        f"{result[0]} = {result[1]} * {numbers[0]} + {result[2]} * {numbers[1]}"
    )

    print(
        result[1] * numbers[0] + result[2] * numbers[1] == result[0]
    )
