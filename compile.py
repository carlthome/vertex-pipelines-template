from kfp import compiler

import pipelines

# Get pipeline function.
pipeline_name = input()
pipeline = getattr(pipelines, pipeline_name)

# Compile pipeline definition.
compiler.Compiler().compile(
    pipeline_func=pipeline,
    package_path=f"./{pipeline_name}.yaml",
)
