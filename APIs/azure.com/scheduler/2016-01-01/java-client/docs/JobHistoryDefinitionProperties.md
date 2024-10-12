

# JobHistoryDefinitionProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actionName** | [**ActionNameEnum**](#ActionNameEnum) | Gets the job history action name. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | Gets the end time for this job. |  [optional] [readonly] |
|**expectedExecutionTime** | **OffsetDateTime** | Gets the expected execution time for this job. |  [optional] [readonly] |
|**message** | **String** | Gets the message for the job history. |  [optional] [readonly] |
|**repeatCount** | **Integer** | Gets the repeat count for the job. |  [optional] [readonly] |
|**retryCount** | **Integer** | Gets the retry count for job. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | Gets the start time for this job. |  [optional] [readonly] |
|**status** | **JobExecutionStatus** |  |  [optional] |



## Enum: ActionNameEnum

| Name | Value |
|---- | -----|
| MAIN_ACTION | &quot;MainAction&quot; |
| ERROR_ACTION | &quot;ErrorAction&quot; |



