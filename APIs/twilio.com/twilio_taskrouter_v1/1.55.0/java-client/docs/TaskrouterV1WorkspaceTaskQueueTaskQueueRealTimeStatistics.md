

# TaskrouterV1WorkspaceTaskQueueTaskQueueRealTimeStatistics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the TaskQueue resource. |  [optional] |
|**activityStatistics** | **List&lt;Object&gt;** | The number of current Workers by Activity. |  [optional] |
|**longestRelativeTaskAgeInQueue** | **Integer** | The relative age in the TaskQueue for the longest waiting Task. Calculation is based on the time when the Task entered the TaskQueue. |  [optional] |
|**longestRelativeTaskSidInQueue** | **String** | The Task SID of the Task waiting in the TaskQueue the longest. Calculation is based on the time when the Task entered the TaskQueue. |  [optional] |
|**longestTaskWaitingAge** | **Integer** | The age of the longest waiting Task. |  [optional] |
|**longestTaskWaitingSid** | **String** | The SID of the longest waiting Task. |  [optional] |
|**taskQueueSid** | **String** | The SID of the TaskQueue from which these statistics were calculated. |  [optional] |
|**tasksByPriority** | **Object** | The number of Tasks by priority. For example: &#x60;{\&quot;0\&quot;: \&quot;10\&quot;, \&quot;99\&quot;: \&quot;5\&quot;}&#x60; shows 10 Tasks at priority 0 and 5 at priority 99. |  [optional] |
|**tasksByStatus** | **Object** | The number of Tasks by their current status. For example: &#x60;{\&quot;pending\&quot;: \&quot;1\&quot;, \&quot;reserved\&quot;: \&quot;3\&quot;, \&quot;assigned\&quot;: \&quot;2\&quot;, \&quot;completed\&quot;: \&quot;5\&quot;}&#x60;. |  [optional] |
|**totalAvailableWorkers** | **Integer** | The total number of Workers available for Tasks in the TaskQueue. |  [optional] |
|**totalEligibleWorkers** | **Integer** | The total number of Workers eligible for Tasks in the TaskQueue, independent of their Activity state. |  [optional] |
|**totalTasks** | **Integer** | The total number of Tasks. |  [optional] |
|**url** | **URI** | The absolute URL of the TaskQueue statistics resource. |  [optional] |
|**workspaceSid** | **String** | The SID of the Workspace that contains the TaskQueue. |  [optional] |



