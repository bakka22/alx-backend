import redis from 'ioredis';

const client = redis.createClient();
client.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
