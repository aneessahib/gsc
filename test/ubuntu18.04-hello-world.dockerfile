From ubuntu:18.04

RUN apt-get update

CMD ["echo", "\"Hello World! Let's check escaped symbols: < & > \""]
