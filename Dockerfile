FROM python:3.10
WORKDIR /Elma
COPY requirements.txt /Elma/
RUN pip install -r requirements.txt
COPY . /Elma
CMD python Elma.py