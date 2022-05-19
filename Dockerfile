FROM python:alpine3.10

RUN mkdir -p /usr/src/app
RUN mkdir -p /usr/src/openapi
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

## install the modules
RUN python3 -m pip install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

COPY /openapi/. /usr/src/openapi
COPY /src/. /usr/src/app

EXPOSE 5001

ENTRYPOINT ["python3"]
CMD ["app.py"]