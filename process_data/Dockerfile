FROM python:3.8-slim
WORKDIR /pipelines
COPY requirements.txt /pipelines
RUN pip install -r requirements.txt
COPY process_data_rul.py /pipelines