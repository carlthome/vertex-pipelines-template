from kfp import dsl


@dsl.component()
def add(num1: int, num2: int) -> int:
    return num1 + num2
