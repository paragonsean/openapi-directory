

# TaskrouterV1WorkspaceWorkspaceRealTimeStatistics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workspace resource. |  [optional] |
|**activityStatistics** | **List&lt;Object&gt;** | The number of current Workers by Activity. |  [optional] |
|**longestTaskWaitingAge** | **Integer** | The age of the longest waiting Task. |  [optional] |
|**longestTaskWaitingSid** | **String** | The SID of the longest waiting Task. |  [optional] |
|**tasksByPriority** | **Object** | The number of Tasks by priority. For example: &#x60;{\&quot;0\&quot;: \&quot;10\&quot;, \&quot;99\&quot;: \&quot;5\&quot;}&#x60; shows 10 Tasks at priority 0 and 5 at priority 99. |  [optional] |
|**tasksByStatus** | **Object** | The number of Tasks by their current status. For example: &#x60;{\&quot;pending\&quot;: \&quot;1\&quot;, \&quot;reserved\&quot;: \&quot;3\&quot;, \&quot;assigned\&quot;: \&quot;2\&quot;, \&quot;completed\&quot;: \&quot;5\&quot;}&#x60;. |  [optional] |
|**totalTasks** | **Integer** | The total number of Tasks. |  [optional] |
|**totalWorkers** | **Integer** | The total number of Workers in the Workspace. |  [optional] |
|**url** | **URI** | The absolute URL of the Workspace statistics resource. |  [optional] |
|**workspaceSid** | **String** | The SID of the Workspace. |  [optional] |



