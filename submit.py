from google.cloud import aiplatform

pipeline_name = "my_pipeline"

# Execute pipeline on Vertex AI Pipelines.
aiplatform.init(
    project="carlthome",
    location="europe-west4",
    experiment="my-experiment",
    experiment_description="my-experiment-description",
)

job = aiplatform.PipelineJob(
    display_name="kfp-pipeline-job",
    template_path=f"./{pipeline_name}.yaml",
    # pipeline_root="gs://<BUCKET_NAME>/kfp_root",
    parameter_values={"a": 1, "b": 2},
    # labels={"runner": "carl"},
    failure_policy="fast",
)

job.submit()
