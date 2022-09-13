FROM python:3.10
MAINTAINER yurasblv.y@gmail.com
WORKDIR /api
COPY requirements.txt /api/
RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

