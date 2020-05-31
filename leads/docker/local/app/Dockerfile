FROM node:12
ENV TZ=America/Caracas
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get install -y \
    build-essential \
    libfontconfig \
    vim \
    && rm -rf /var/lib/apt/lists/*
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY ./leads .
RUN npm install -g sequelize-cli nodemon
RUN npm install
EXPOSE 8001
CMD [ "npm", "run", "start:dev" ]

