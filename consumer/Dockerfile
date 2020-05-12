FROM python:3
ADD receive.py /
RUN pip install pika
CMD ["python","-u","receive.py"]
