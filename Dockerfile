FROM python:3:11.7

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . ./

EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]