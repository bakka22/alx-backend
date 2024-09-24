import redis from 'ioredis';

const sub = redis.createClient();
sub.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

sub.on('connect', () => {
  console.log('Redis client connected to the server');
});

sub.subscribe('holberton school channel', (err) => {
  if (err) {
    throw new Error(err);
  }
});

sub.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    sub.unsubscribe('holberton school channel');
    sub.quit();
  }
});
