from kfp import dsl


@dsl.component(
    base_image="python:3.8",
    target_image="gcr.io/carlthome/kfp-addition:latest",
)
def train2(
    num1: int, num2: int, model: dsl.Output[dsl.Model], metrics: dsl.Output[dsl.Metrics]
) -> int:
    return "hello"


@dsl.component(
    base_image="python:3.8",
    target_image="gcr.io/carlthome/kfp-addition:latest",
)
def train(
    num1: int, num2: int, model: dsl.Output[dsl.Model], metrics: dsl.Output[dsl.Metrics]
) -> int:
    import tensorflow as tf

    num1 = tf.constant(num1)
    num2 = tf.constant(num2)

    metrics.log_metric("accuracy", 0.9)

    with open(model.path, "w") as f:
        f.write("hello world")
    return num1 + num2
