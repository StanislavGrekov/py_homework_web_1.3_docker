FROM debian:11

MAINTAINER GrekovStas

RUN apt-get update && apt-get install -y \
    python3.9 \
    python3-pip

COPY . ./app
WORKDIR /app
RUN chmod +x script.sh
RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ./script.sh
