FROM python:3.8-slim-buster

COPY net_interface_monitor.py . 

COPY requirements.txt . 

RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD [ "python", "-u", "./net_interface_monitor.py" ]
