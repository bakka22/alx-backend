import kue from 'kue';

const queue = kue.createQueue();

// Create a job
const job = queue.create('email', {
  title: 'Welcome Email',
  to: 'user@example.com',
  template: 'welcome-email'
}).save(err => {
  if (!err) console.log(`Job created: ${job.id}`);
});

