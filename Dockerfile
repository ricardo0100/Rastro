FROM python:alpine
ADD ./webapp/requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
WORKDIR /opt/webapp
EXPOSE 5000
CMD ["python", "app.py"]
