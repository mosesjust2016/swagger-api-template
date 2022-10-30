  
FROM python:3.8

COPY ./ /api
WORKDIR /api
RUN set -ex && \
    pip install -r requirements.txt
EXPOSE 8899
CMD ["python", "server.py"]