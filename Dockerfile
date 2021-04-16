FROM python:3.7-slim

RUN pip install pyyaml

ADD . /app

ENTRYPOINT ["python", "/app/kubeconfig.py"]
