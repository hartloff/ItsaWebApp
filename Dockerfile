FROM python:3.8

ENV HOME /root
WORKDIR /root

COPY . .

RUN pip install -r requirements.txt

CMD python3 app.py