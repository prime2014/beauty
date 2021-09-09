FROM node:14.5.0

WORKDIR /app

COPY ./beauty/package.json /app/

COPY ./beauty/* /app/

RUN npm install

ENV PATH ./node_modules/.bin/:$PATH
