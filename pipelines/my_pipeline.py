from kfp import dsl

# from components.python import add
from components.pytorch import add


@dsl.pipeline()
def my_pipeline(a: int, b: int, c: int = 10):
    add_task_0 = add(num1=a, num2=b)

    add_task_1 = add(num1=add_task_0.output, num2=b)
