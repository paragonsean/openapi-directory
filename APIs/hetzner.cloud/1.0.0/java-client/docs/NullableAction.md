

# NullableAction


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**command** | **String** | Command executed in the Action |  |
|**error** | [**ActionError**](ActionError.md) |  |  |
|**finished** | **String** | Point in time when the Action was finished (in ISO-8601 format). Only set if the Action is finished otherwise null. |  |
|**id** | **Integer** | ID of the Resource |  |
|**progress** | **BigDecimal** | Progress of Action in percent |  |
|**resources** | [**List&lt;ActionResourcesInner&gt;**](ActionResourcesInner.md) | Resources the Action relates to |  |
|**started** | **String** | Point in time when the Action was started (in ISO-8601 format) |  |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the Action |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| SUCCESS | &quot;success&quot; |
| RUNNING | &quot;running&quot; |
| ERROR | &quot;error&quot; |



