FROM node:16.15-alpine
WORKDIR /frontend_app
COPY . /frontend_app
ENV PATH /frontend_app/node_modules/.bin:$PATH
RUN yarn install
CMD ["yarn", "start"]
