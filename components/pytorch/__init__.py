from kfp import dsl


@dsl.component(
    target_image="europe-docker.pkg.dev/vertex-ai/training/pytorch-xla.1-11:latest"
)
def add(num1: int, num2: int) -> int:
    import torch

    num1 = torch.constant(num1)
    num2 = torch.constant(num2)

    return num1 + num2
