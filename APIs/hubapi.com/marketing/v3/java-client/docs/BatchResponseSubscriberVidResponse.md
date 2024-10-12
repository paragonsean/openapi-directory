

# BatchResponseSubscriberVidResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedAt** | **OffsetDateTime** |  |  |
|**errors** | [**List&lt;StandardError&gt;**](StandardError.md) |  |  [optional] |
|**links** | **Map&lt;String, String&gt;** |  |  [optional] |
|**numErrors** | **Integer** |  |  [optional] |
|**requestedAt** | **OffsetDateTime** |  |  [optional] |
|**results** | [**List&lt;SubscriberVidResponse&gt;**](SubscriberVidResponse.md) |  |  |
|**startedAt** | **OffsetDateTime** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| CANCELED | &quot;CANCELED&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



