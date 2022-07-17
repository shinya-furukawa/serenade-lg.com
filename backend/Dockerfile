FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV APP_ROOT /code
WORKDIR ${APP_ROOT}
COPY . ${APP_ROOT}
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt