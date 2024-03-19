FROM python:3.10-alpine

WORKDIR /src/

COPY ./fastapi_app/requirements.txt /src/requirements.txt

RUN pip install -r --no-cache-dir requirements.txt

COPY ./fastapi_app /src/

EXPOSE 8001

CMD [ "uvicorn", "main:app", "--port", "8001", "--host", "0.0.0.0" ]