FROM python:3.10
COPY ./requirements.txt /consumer2/requirements.txt
WORKDIR /consumer2
RUN pip install -r requirements.txt
COPY . /consumer2
ENTRYPOINT [ "python","app.py" ]