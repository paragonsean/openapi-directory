

# TaskStatus

TaskStatus represents the status of a task.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completionTime** | **String** | Optional. Represents time when the task was completed. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. |  [optional] |
|**conditions** | [**List&lt;GoogleCloudRunV1Condition&gt;**](GoogleCloudRunV1Condition.md) | Optional. Conditions communicate information about ongoing/complete reconciliation processes that bring the \&quot;spec\&quot; inline with the observed state of the world. Task-specific conditions include: * &#x60;Started&#x60;: &#x60;True&#x60; when the task has started to execute. * &#x60;Completed&#x60;: &#x60;True&#x60; when the task has succeeded. &#x60;False&#x60; when the task has failed. |  [optional] |
|**index** | **Integer** | Required. Index of the task, unique per execution, and beginning at 0. |  [optional] |
|**lastAttemptResult** | [**TaskAttemptResult**](TaskAttemptResult.md) |  |  [optional] |
|**logUri** | **String** | Optional. URI where logs for this task can be found in Cloud Console. |  [optional] |
|**observedGeneration** | **Integer** | Optional. The &#39;generation&#39; of the task that was last processed by the controller. |  [optional] |
|**retried** | **Integer** | Optional. The number of times this task was retried. Instances are retried when they fail up to the maxRetries limit. |  [optional] |
|**startTime** | **String** | Optional. Represents time when the task started to run. It is not guaranteed to be set in happens-before order across separate operations. It is represented in RFC3339 form and is in UTC. |  [optional] |



