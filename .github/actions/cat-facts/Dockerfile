FROM python:3

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.text

COPY . .

CMD [ "python", "/src/main.py"]
