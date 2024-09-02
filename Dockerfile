FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

RUN pip install flake8 coverage
RUN flake8 .
RUN coverage run manage.py test
RUN coverage report

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]