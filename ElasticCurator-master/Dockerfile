FROM python:2.7.8-slim

RUN pip install --quiet elasticsearch-curator==5.4.0

ADD curator /curator

WORKDIR /curator

ENTRYPOINT [ "/usr/local/bin/curator" ]