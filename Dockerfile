FROM alpine:3.2

RUN apk add --update musl python3 py-pip bash && \
    rm /var/cache/apk/*

ADD requirements.txt /
COPY wedrmedr/unsplash /unsplash

RUN pip install -r /requirements.txt

EXPOSE 5000 8000 80
WORKDIR /

CMD ["gunicorn", "-b", "0.0.0.0:8000", "-w", "4", "unsplash.client:API"]

