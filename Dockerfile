FROM python:3.11-slim-buster

RUN apt-get update \
  && apt-get install -y gcc \
  && apt-get install -y build-essential \
  && apt-get install -y libpq-dev libffi-dev \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PROJECT_ROOT /usr/src/app
ENV PYTHONPATH "${PYTHONPATH}:${PROJECT_ROOT}"

RUN mkdir -p ${PROJECT_ROOT}
COPY ./src/ ${PROJECT_ROOT}

WORKDIR ${PROJECT_ROOT}

COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD ["python", "employee_app/app.py"]
