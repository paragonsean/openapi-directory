

# OrderRefundsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Integer** |  |  [optional] |
|**currency** | **Currency** |  |  [optional] |
|**id** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**locationId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**reason** | **String** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) |  |  [optional] |
|**tenderId** | **String** | A unique identifier for an object. |  [optional] [readonly] |
|**transactionId** | **String** | A unique identifier for an object. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PENDING | &quot;pending&quot; |
| APPROVED | &quot;approved&quot; |
| REJECTED | &quot;rejected&quot; |
| FAILED | &quot;failed&quot; |



