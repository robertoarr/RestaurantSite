FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code && mkdir my-tools
WORKDIR /code

ADD ./ /code/

RUN \
    # apk update && \
    pip install --upgrade pip && \
    pip install -r requirements.txt --no-cache-dir
    # apk del .build-deps
    # ADD ./test_responsive /code/

RUN \
    wget https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    rm chromedriver_linux64.zip

RUN \
    curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add &&\
    echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list &&\
    apt-get -y update &&\
    apt-get -y install google-chrome-stable &&\
    apt-get install -y libnss3

ENTRYPOINT ["/entrypoint.sh"]
# ENTRYPOINT ["python", "main.py"]
