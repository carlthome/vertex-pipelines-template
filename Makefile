my_pipeline.yaml: pipelines/my_pipeline.py
	echo my_pipeline | python compile.py


submit:
	python submit.py