

# JobFilter

Contains the information about the filters for the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**startTime** | **OffsetDateTime** | The start time of the job. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The status of the job. |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| WAITING_FOR_ACTION | &quot;WaitingForAction&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| CANCELLING | &quot;Cancelling&quot; |



