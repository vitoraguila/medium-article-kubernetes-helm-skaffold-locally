FROM golang:1.15-alpine as dev

WORKDIR /work

FROM golang:1.15-alpine as build

WORKDIR /users
COPY ./users/* /users/
RUN go build -o users

FROM alpine as runtime 
COPY --from=build /users/users /
COPY ./users/users.json /
CMD ./users