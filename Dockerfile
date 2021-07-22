FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /var/www/aiohttp/
WORKDIR /var/www/aiohttp/

COPY . /var/www/aiohttp/
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ['python', './app.py']