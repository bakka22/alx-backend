import Redis from 'ioredis'; // Using import instead of require

const redis = new Redis();

// Synchronous-like usage (still async internally)
redis.set('myKey', 'myValue')
  .then(result => {
    console.log(result); // Logs 'OK'
  })
  .catch(err => {
    console.error(err);
  });
