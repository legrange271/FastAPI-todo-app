FROM python:3.10-alpine

WORKDIR /src/

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir --upgrade -r  requirements.txt

COPY ./src/ /src/

EXPOSE 8001

CMD [ "uvicorn", "main:app", "--port", "8001", "--host", "0.0.0.0" ]