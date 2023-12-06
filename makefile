python:
	python3 -B main.py

docker:
	docker build -t rlt .

rd:
	docker run -it --rm rlt