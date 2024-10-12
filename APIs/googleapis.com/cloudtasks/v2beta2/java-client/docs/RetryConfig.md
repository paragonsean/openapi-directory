

# RetryConfig

Retry config. These settings determine how a failed task attempt is retried.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxAttempts** | **Integer** | The maximum number of attempts for a task. Cloud Tasks will attempt the task &#x60;max_attempts&#x60; times (that is, if the first attempt fails, then there will be &#x60;max_attempts - 1&#x60; retries). Must be &gt; 0. |  [optional] |
|**maxBackoff** | **String** | A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue&#39;s RetryConfig specifies that the task should be retried. If unspecified when the queue is created, Cloud Tasks will pick the default. This field is output only for pull queues. &#x60;max_backoff&#x60; will be truncated to the nearest second. This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). |  [optional] |
|**maxDoublings** | **Integer** | The time between retries will double &#x60;max_doublings&#x60; times. A task&#39;s retry interval starts at min_backoff, then doubles &#x60;max_doublings&#x60; times, then increases linearly, and finally retries at intervals of max_backoff up to max_attempts times. For example, if min_backoff is 10s, max_backoff is 300s, and &#x60;max_doublings&#x60; is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of max_backoff until the task has been attempted max_attempts times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, .... If unspecified when the queue is created, Cloud Tasks will pick the default. This field is output only for pull queues. This field has the same meaning as [max_doublings in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). |  [optional] |
|**maxRetryDuration** | **String** | If positive, &#x60;max_retry_duration&#x60; specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once &#x60;max_retry_duration&#x60; time has passed *and* the task has been attempted max_attempts times, no further attempts will be made and the task will be deleted. If zero, then the task age is unlimited. If unspecified when the queue is created, Cloud Tasks will pick the default. This field is output only for pull queues. &#x60;max_retry_duration&#x60; will be truncated to the nearest second. This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). |  [optional] |
|**minBackoff** | **String** | A task will be scheduled for retry between min_backoff and max_backoff duration after it fails, if the queue&#39;s RetryConfig specifies that the task should be retried. If unspecified when the queue is created, Cloud Tasks will pick the default. This field is output only for pull queues. &#x60;min_backoff&#x60; will be truncated to the nearest second. This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). |  [optional] |
|**unlimitedAttempts** | **Boolean** | If true, then the number of attempts is unlimited. |  [optional] |



