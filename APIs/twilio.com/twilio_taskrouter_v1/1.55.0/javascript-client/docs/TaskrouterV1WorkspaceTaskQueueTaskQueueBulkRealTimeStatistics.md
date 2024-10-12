# TwilioTaskrouter.TaskrouterV1WorkspaceTaskQueueTaskQueueBulkRealTimeStatistics

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource. | [optional] 
**taskQueueData** | **[Object]** | The real-time statistics for each requested TaskQueue SID. &#x60;task_queue_data&#x60; returns the following attributes:  &#x60;task_queue_sid&#x60;: The SID of the TaskQueue from which these statistics were calculated.  &#x60;total_available_workers&#x60;: The total number of Workers available for Tasks in the TaskQueue.  &#x60;total_eligible_workers&#x60;: The total number of Workers eligible for Tasks in the TaskQueue, regardless of their Activity state.  &#x60;total_tasks&#x60;: The total number of Tasks.  &#x60;longest_task_waiting_age&#x60;: The age of the longest waiting Task.  &#x60;longest_task_waiting_sid&#x60;: The SID of the longest waiting Task.  &#x60;tasks_by_status&#x60;: The number of Tasks grouped by their current status.  &#x60;tasks_by_priority&#x60;: The number of Tasks grouped by priority.  &#x60;activity_statistics&#x60;: The number of current Workers grouped by Activity.  | [optional] 
**taskQueueResponseCount** | **Number** | The number of TaskQueue statistics received in task_queue_data. | [optional] 
**url** | **String** | The absolute URL of the TaskQueue statistics resource. | [optional] 
**workspaceSid** | **String** | The SID of the Workspace that contains the TaskQueue. | [optional] 


