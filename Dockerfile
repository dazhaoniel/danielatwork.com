FROM python:3.10-slim-bullseye AS pelican

EXPOSE 80

RUN apt update && apt install -y --no-install-recommends git \
  make \
  && rm -rf /var/lib/apt/lists/*

ADD requirements.txt requirements.txt
RUN python -m pip install --no-cache-dir -r requirements.txt

# prevent writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# bust the cache 
WORKDIR /website 
COPY . /website/

RUN pelican

FROM httpd:2.4.52-alpine
COPY --from=pelican /website/output/ /usr/local/apache2/htdocs/