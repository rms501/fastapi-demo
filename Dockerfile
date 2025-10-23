FROM python:3.13
WORKDIR /usr/local/app

COPY ./ ./
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 8080

RUN useradd app
USER app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]