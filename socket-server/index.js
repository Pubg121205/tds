const express = require('express');
const http = require('http');
const socketIO = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIO(server);

const players = {};

io.on('connection', socket => {
  console.log('🔗 New player:', socket.id);
  players[socket.id] = {
    id: socket.id,
    x: 0, y: 0, z: 0,
    rotY: 0,
    hp: 100
  };

  socket.emit('init', { id: socket.id, players });
  socket.broadcast.emit('newPlayer', players[socket.id]);

  socket.on('update', data => {
    if (players[socket.id]) {
      Object.assign(players[socket.id], data);
      io.emit('playerUpdate', players[socket.id]);
    }
  });

  socket.on('skill', data => {
    io.emit('playerSkill', { id: socket.id, skill: data.skill });
  });

  socket.on('disconnect', () => {
    delete players[socket.id];
    io.emit('removePlayer', socket.id);
    console.log('❌ Player gone', socket.id);
  });
});

const PORT = process.env.PORT || 10000;
server.listen(PORT, () => console.log(`🚀 Server running on port ${PORT}`));