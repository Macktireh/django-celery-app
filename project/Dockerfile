# pull official base image
FROM python:3.12.3-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# copy project
COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
