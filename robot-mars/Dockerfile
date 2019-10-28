FROM python:3.7.3

ADD *.py /

RUN pip install --upgrade pip

RUN pip install keyboard
RUN pip install requests

CMD [ "python", "./main.py" ]
