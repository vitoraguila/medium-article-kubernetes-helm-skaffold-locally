'use strict';

const express = require('express');
const users = require('./users.json');

const PORT = 3000;

const app = express();

app.get('/api/nodejs/users', (req, res) => {
  res.send(users);
});


app.listen(PORT);

console.log(`Running version 3 on Port: ${PORT}`);