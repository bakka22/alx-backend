import kue from 'kue';

const queue = kue.createQueue();

queue.process('email', (job, done) => {
  // Simulate email sending
  console.log(`Sending email to ${job.data.to}`);
  
  // Simulate success
  done(); // Call done() to indicate job completion
  // Call done(err) to indicate job failure with an error
});

