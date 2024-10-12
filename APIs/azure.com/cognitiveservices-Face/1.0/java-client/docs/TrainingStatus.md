

# TrainingStatus

Training status object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDateTime** | **OffsetDateTime** | A combined UTC date and time string that describes the created time of the person group, large person group or large face list. |  |
|**lastActionDateTime** | **OffsetDateTime** | A combined UTC date and time string that describes the last modify time of the person group, large person group or large face list, could be null value when the group is not successfully trained. |  [optional] |
|**lastSuccessfulTrainingDateTime** | **OffsetDateTime** | A combined UTC date and time string that describes the last successful training time of the person group, large person group or large face list. |  [optional] |
|**message** | **String** | Show failure message when training failed (omitted when training succeed). |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Training status: notstarted, running, succeeded, failed. If the training process is waiting to perform, the status is notstarted. If the training is ongoing, the status is running. Status succeed means this person group or large person group is ready for Face - Identify, or this large face list is ready for Face - Find Similar. Status failed is often caused by no person or no persisted face exist in the person group or large person group, or no persisted face exist in the large face list. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NONSTARTED | &quot;nonstarted&quot; |
| RUNNING | &quot;running&quot; |
| SUCCEEDED | &quot;succeeded&quot; |
| FAILED | &quot;failed&quot; |



