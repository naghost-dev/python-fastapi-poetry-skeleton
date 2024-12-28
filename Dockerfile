# (1)
FROM python:3.11-slim as requirements-stage

# (2)
WORKDIR /tmp

# (3)
RUN pip install poetry

# (4)
COPY ./pyproject.toml ./poetry.lock* /tmp/

# (5)
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --without dev,test --with docker

# (6)
FROM python:3.11-slim

# (7)
WORKDIR /code

# (8)
COPY --from=requirements-stage /tmp/requirements.txt /code/requirements.txt

# (9)
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# (10)
COPY ./src /code/src

COPY gunicorn.conf.py /code/gunicorn.conf.py
# (11)
CMD ["gunicorn", "src.app.main:app", "-c", "gunicorn.conf.py"]