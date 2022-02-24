FROM python:3.8.11
ARG DEBIAN_FRONTEND=noninteractive

EXPOSE 9000

WORKDIR /opt/server

ADD requirements.txt /opt/server
RUN pip install -r requirements.txt

ADD main.py /opt/server
ADD plato_mini.py /opt/server

# run script to download the required models into cache
RUN python plato_mini.py

CMD ["uvicorn", "main:app", "-p", "9000"]
