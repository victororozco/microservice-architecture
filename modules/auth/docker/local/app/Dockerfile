FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN apt-get install -y bash

RUN mkdir /code
WORKDIR /code

# Requirements are installed here to ensure they will be cached.
COPY ./modules/auth/requirements /code/requirements
RUN pip install -r /code/requirements/common.txt

COPY ./modules/auth/docker/local/app/entrypoint.sh /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint

COPY ./modules/auth/docker/local/app/start.sh /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

EXPOSE 8000
CMD ["/entrypoint"]