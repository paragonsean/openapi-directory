

# BatchResponseSubscriptionResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**completedAt** | **OffsetDateTime** |  |  |
|**links** | **Map&lt;String, String&gt;** |  |  [optional] |
|**requestedAt** | **OffsetDateTime** |  |  [optional] |
|**results** | [**List&lt;SubscriptionResponse&gt;**](SubscriptionResponse.md) |  |  |
|**startedAt** | **OffsetDateTime** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;PENDING&quot; |
| PROCESSING | &quot;PROCESSING&quot; |
| CANCELED | &quot;CANCELED&quot; |
| COMPLETE | &quot;COMPLETE&quot; |



