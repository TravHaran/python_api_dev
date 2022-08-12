FROM python:3.9.6

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ADD start.sh /
RUN chmod +x /start.sh

CMD ["/start.sh"]

