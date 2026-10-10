FROM python:3.12-alpine
WORKDIR /app
RUN pip install flask gunicorn
COPY . .
EXPOSE 5000
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]