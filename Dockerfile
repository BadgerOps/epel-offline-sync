FROM registry.access.redhat.com/ubi9/python-39@sha256:195c51368e83a798b6f79c6a5d877685fdf5297a81e5211cfca747a7fca725aa

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]