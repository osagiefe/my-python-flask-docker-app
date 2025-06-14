FROM python:alpine
ADD . /main
WORKDIR /main
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8081
ENTRYPOINT ["python","main.py"]
