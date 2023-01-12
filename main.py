from google.cloud import aiplatform
from kfp import compiler, dsl


@dsl.component(
    base_image="python:3.7",
    packages_to_install=["tensorflow"],
    target_image="gcr.io/carlthome/kfp-addition:latest",
)
def addition_component(num1: int, num2: int) -> int:
    import tensorflow as tf

    num1 = tf.constant(num1)
    num2 = tf.constant(num2)
    return num1 + num2


@dsl.pipeline()
def my_pipeline(a: int, b: int, c: int = 10):
    add_task_1 = addition_component(num1=a, num2=b)
    add_task_2 = addition_component(num1=add_task_1.output, num2=c)
    return add_task_2


if __name__ == "__main__":

    # Compile pipeline definition.
    compiler.Compiler().compile(
        pipeline_func=my_pipeline,
        package_path="./pipeline.yaml",
    )

    # Execute pipeline on Vertex AI Pipelines.
    aiplatform.init(
        project="carlthome",
        location="europe-west4",
        experiment="my-experiment",
        experiment_description="my-experiment-description",
    )

    job = aiplatform.PipelineJob(
        display_name="kfp-pipeline-job",
        template_path="./pipeline.yaml",
        # pipeline_root="gs://<BUCKET_NAME>/kfp_root",
        parameter_values={"a": 1, "b": 2},
        # labels={"runner": "carl"},
    )

    job.submit()
    # job.wait()
