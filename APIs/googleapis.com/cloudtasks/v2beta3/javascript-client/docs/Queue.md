# CloudTasksApi.Queue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appEngineHttpQueue** | [**AppEngineHttpQueue**](AppEngineHttpQueue.md) |  | [optional] 
**httpTarget** | [**HttpTarget**](HttpTarget.md) |  | [optional] 
**name** | **String** | Caller-specified and required in CreateQueue, after which it becomes output only. The queue name. The queue name must have the following format: &#x60;projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID&#x60; * &#x60;PROJECT_ID&#x60; can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) * &#x60;LOCATION_ID&#x60; is the canonical ID for the queue&#39;s location. The list of available locations can be obtained by calling ListLocations. For more information, see https://cloud.google.com/about/locations/. * &#x60;QUEUE_ID&#x60; can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters. | [optional] 
**purgeTime** | **String** | Output only. The last time this queue was purged. All tasks that were created before this time were purged. A queue can be purged using PurgeQueue, the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue). Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged. | [optional] 
**rateLimits** | [**RateLimits**](RateLimits.md) |  | [optional] 
**retryConfig** | [**RetryConfig**](RetryConfig.md) |  | [optional] 
**stackdriverLoggingConfig** | [**StackdriverLoggingConfig**](StackdriverLoggingConfig.md) |  | [optional] 
**state** | **String** | Output only. The state of the queue. &#x60;state&#x60; can only be changed by called PauseQueue, ResumeQueue, or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). UpdateQueue cannot be used to change &#x60;state&#x60;. | [optional] 
**stats** | [**QueueStats**](QueueStats.md) |  | [optional] 
**taskTtl** | **String** | The maximum amount of time that a task will be retained in this queue. After a task has lived for &#x60;task_ttl&#x60;, the task will be deleted regardless of whether it was dispatched or not. The minimum value is 10 days. The maximum value is 10 years. The value must be given as a string that indicates the length of time (in seconds) followed by &#x60;s&#x60; (for \&quot;seconds\&quot;). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). Queues created by Cloud Tasks have a default &#x60;task_ttl&#x60; of 31 days. . Queues created by queue.yaml/xml have a fixed &#x60;task_ttl&#x60; of the maximum duration, because there is a [storage quota](https://cloud.google.com/appengine/quotas#Task_Queue) for these queues. | [optional] 
**tombstoneTtl** | **String** | The task tombstone time to live (TTL). After a task is deleted or executed, the task&#39;s tombstone is retained for the length of time specified by &#x60;tombstone_ttl&#x60;. The tombstone is used by task de-duplication; another task with the same name can&#39;t be created until the tombstone has expired. For more information about task de-duplication, see the documentation for CreateTaskRequest. The minimum value is 1 hour. The maximum value is 9 days. The value must be given as a string that indicates the length of time (in seconds) followed by &#x60;s&#x60; (for \&quot;seconds\&quot;). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). Queues created by Cloud Tasks have a default &#x60;tombstone_ttl&#x60; of 1 hour. | [optional] 
**type** | **String** | Immutable. The type of a queue (push or pull). &#x60;Queue.type&#x60; is an immutable property of the queue that is set at the queue creation time. When left unspecified, the default value of &#x60;PUSH&#x60; is selected. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `PAUSED` (value: `"PAUSED"`)

* `DISABLED` (value: `"DISABLED"`)





## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `PULL` (value: `"PULL"`)

* `PUSH` (value: `"PUSH"`)




