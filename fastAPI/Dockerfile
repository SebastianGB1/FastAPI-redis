FROM python:3.10
COPY ./requirements.txt /fastAPI/requirements.txt
WORKDIR /fastAPI
RUN pip install -r requirements.txt
COPY . /fastAPI
ENTRYPOINT [ "uvicorn","app:app" ]
CMD [ "--host=0.0.0.0" ]