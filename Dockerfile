FROM python:3.11-slim

WORKDIR /mtgjson

COPY ./mtgjson5 ./mtgjson5
COPY ./requirements.txt ./requirements.txt

RUN apt-get update \
    && apt-get install -y --no-install-recommends git bzip2 xz-utils zip htop  \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r ./requirements.txt pip

ENTRYPOINT ["python3", "-m", "mtgjson5", "--use-envvars"]
