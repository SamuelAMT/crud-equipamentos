FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/

ARG DB_NAME
ARG DB_ENGINE

ENV DB_NAME=${DB_NAME}
ENV DB_ENGINE=${DB_ENGINE}

EXPOSE 8000

CMD ["gunicorn", "ArkmedsEquipamentos.wsgi:application", "--bind", "0.0.0.0:8000"]
