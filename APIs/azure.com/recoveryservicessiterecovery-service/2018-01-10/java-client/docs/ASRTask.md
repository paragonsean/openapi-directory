

# ASRTask

Task of the Job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedActions** | **List&lt;String&gt;** | The state/actions applicable on this task. |  [optional] |
|**customDetails** | [**TaskTypeDetails**](TaskTypeDetails.md) |  |  [optional] |
|**endTime** | **OffsetDateTime** | The end time. |  [optional] |
|**errors** | [**List&lt;JobErrorDetails&gt;**](JobErrorDetails.md) | The task error details. |  [optional] |
|**friendlyName** | **String** | The name. |  [optional] |
|**groupTaskCustomDetails** | [**GroupTaskDetails**](GroupTaskDetails.md) |  |  [optional] |
|**name** | **String** | The unique Task name. |  [optional] |
|**startTime** | **OffsetDateTime** | The start time. |  [optional] |
|**state** | **String** | The State. It is one of these values - NotStarted, InProgress, Succeeded, Failed, Cancelled, Suspended or Other. |  [optional] |
|**stateDescription** | **String** | The description of the task state. For example - For Succeeded state, description can be Completed, PartiallySucceeded, CompletedWithInformation or Skipped. |  [optional] |
|**taskId** | **String** | The Id. |  [optional] |
|**taskType** | **String** | The type of task. Details in CustomDetails property depend on this type. |  [optional] |



