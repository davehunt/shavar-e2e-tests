FROM selenium/standalone-firefox

USER root

WORKDIR /tests

RUN apt-get -qqy update && apt-get install -qqy \ 
    git \
    python \
    python-dev \
    python-pip \ 
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/*

RUN pip install --upgrade pip && pip install tox 

COPY . /tests
WORKDIR /tests
CMD tox itisatrap 
