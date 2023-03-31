# 
FROM python:3.11.2

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt

# 
RUN python3 -m venv ./venv 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


# 
COPY ./ /code

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

