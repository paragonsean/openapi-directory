

# TaskrouterV1WorkspaceWorkflowWorkflowRealTimeStatistics


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountSid** | **String** | The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Workflow resource. |  [optional] |
|**longestTaskWaitingAge** | **Integer** | The age of the longest waiting Task. |  [optional] |
|**longestTaskWaitingSid** | **String** | The SID of the longest waiting Task. |  [optional] |
|**tasksByPriority** | **Object** | The number of Tasks by priority. For example: &#x60;{\&quot;0\&quot;: \&quot;10\&quot;, \&quot;99\&quot;: \&quot;5\&quot;}&#x60; shows 10 Tasks at priority 0 and 5 at priority 99. |  [optional] |
|**tasksByStatus** | **Object** | The number of Tasks by their current status. For example: &#x60;{\&quot;pending\&quot;: \&quot;1\&quot;, \&quot;reserved\&quot;: \&quot;3\&quot;, \&quot;assigned\&quot;: \&quot;2\&quot;, \&quot;completed\&quot;: \&quot;5\&quot;}&#x60;. |  [optional] |
|**totalTasks** | **Integer** | The total number of Tasks. |  [optional] |
|**url** | **URI** | The absolute URL of the Workflow statistics resource. |  [optional] |
|**workflowSid** | **String** | Returns the list of Tasks that are being controlled by the Workflow with the specified SID value. |  [optional] |
|**workspaceSid** | **String** | The SID of the Workspace that contains the Workflow. |  [optional] |



