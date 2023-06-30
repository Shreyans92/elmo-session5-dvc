FROM python:3.9-slim

WORKDIR /workspace/project-setup

COPY requirements.txt requirements.txt

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN pip install -e .

CMD ["python", "dummypackage/train.py" , "dummypackage/eval.py"]