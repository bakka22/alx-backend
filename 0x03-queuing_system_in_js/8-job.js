export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }
  for (const data of jobs) {
    const job = queue.create('push_notification_code_3', data).save(err => {
      if (!err) {
        console.log(`Notification job created: ${job.id}`);
        job.on('complete', (result) => {
          console.log(`Notification job #${job.id} completed`);
        });

        job.on('failed', (errMsg) => {
          console.log(`Notification job #${job.id} faild: ${errMsg}`);
        });

        job.on('progress', (progress) => {
          console.log(`Notification job #${job.id} ${progress}% complete`);
        });
      }
    });
  }
}
