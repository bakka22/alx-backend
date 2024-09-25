import redis from 'ioredis';
import { promisify } from 'util';
import kue from 'kue';
import express from 'express';

// ---------------redis---------------
const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

function reserveSeat (number) {
  client.set('available_seats', number);
}

async function getCurrentAvailableSeats () {
  const getAsync = promisify(client.get).bind(client);
  const value = await getAsync('available_seats');
  return value;
}

reserveSeat(50);
let reservationEnabled = true;

// ---------------kue-----------
const queue = kue.createQueue();

// --------------express server----------
const app = express();
const port = 1245;

app.get('/available_seats', async (req, res) => {
  const seatCount = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: seatCount });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }
  const job = queue.create('reserve_seat').save(err => {
    if (!err) {
      job.on('complete', () => {
        console.log(`Seat reservation job #${job.id} completed`);
      });

      job.on('failed', (errMsg) => {
        console.log(`Seat reservation job #${job.id} faild: ${errMsg}`);
      });
      return res.json({ status: 'Reservation in process' });
    }
    return res.json({ status: 'Reservation failed' });
  });
});

app.get('/process', (req, res) => {
  queue.process('reserve_seat', async (job, done) => {
    const seatsAvailable = await getCurrentAvailableSeats();
    if (seatsAvailable === 0) {
      done(new Error('Not enough seats available'));
    }
    if (seatsAvailable === 1) {
      reservationEnabled = false;
    }
    reserveSeat(seatsAvailable - 1);
    done();
  });
  res.json({ status: 'Queue processing' });
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
