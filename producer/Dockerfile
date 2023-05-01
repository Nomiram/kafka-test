FROM python:3.10
COPY requiroments.txt .
RUN pip install -r requiroments.txt
COPY kafka-produser.py /
CMD [ "python3", "kafka-produser.py" ]