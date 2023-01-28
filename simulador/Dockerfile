FROM python:3.10
COPY ./requirements.txt /simulator/requirements.txt
WORKDIR /simulator
RUN pip install -r requirements.txt
COPY . /simulator
ENTRYPOINT [ "python","app.py" ]