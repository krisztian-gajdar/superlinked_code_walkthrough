FROM python:latest
WORKDIR /app
COPY . /app
RUN pip install .
CMD ["uvicorn", "tier_backend.main:app", "--host", "0.0.0.0", "--port", "80"]
