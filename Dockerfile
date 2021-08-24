FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

COPY ./echo_server/app /app/app
