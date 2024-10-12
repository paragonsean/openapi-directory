

# DataSubjectRightUpdateStatusOperation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**participantData** | **String** | String field to be used by participant for any intermediate statuses or data they need to save |  [optional] |
|**requestId** | **String** | Request identifier of the operation |  |
|**status** | [**StatusEnum**](#StatusEnum) | Operation status |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| CREATED | &quot;Created&quot; |
| QUEUED | &quot;Queued&quot; |
| IN_PROGRESS | &quot;InProgress&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAILED | &quot;Failed&quot; |



