FROM python:3
RUN git clone https://github.com/temPLAY333/CRUD-Persona
WORKDIR /CRUD-Persona
RUN pip install -r requirements.txt
CMD ["python3" ,"-m",  "unittest"]
