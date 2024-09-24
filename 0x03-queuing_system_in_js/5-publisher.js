import redis from 'ioredis';

const pub = redis.createClient();
pub.on('error', err => {
  console.log(`Redis client not connected to the server: ${err}`);
});

pub.on('connect', () => {
  console.log('Redis client connected to the server');
});

function publishMessage (message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    pub.publish('holberton school channel', message, (err) => {
      if (err) {
        throw new Error(err);
      }
    });
  }, time);
}

publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
