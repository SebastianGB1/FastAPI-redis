FROM python:3.10
COPY ./requirements.txt /consumer1/requirements.txt
WORKDIR /consumer1
RUN pip install -r requirements.txt
COPY . /consumer1
ENTRYPOINT [ "python","app.py" ]