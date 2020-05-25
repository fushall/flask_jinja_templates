# base container
FROM python:3.7-slim-stretch

# timezone
ENV TZ Asia/Shanghai

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ -r /code/requirements.txt \
    && rm -rf /tmp \
    && rm -rf ~/.cache/pip/wheels

COPY . /code/

WORKDIR /code

CMD gunicorn -b 0.0.0.0:8080 --log-level info --access-logfile - web:app