

# BlockListRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**countDetails** | **Boolean** | If true it will include also details of block count per each room type. |  [optional] |
|**from** | **OffsetDateTime** | Return all blocks where the block&#39;s last_departure is greater than specified date. |  [optional] |
|**groupCode** | **String** | Filter the blocks by the specified group code |  [optional] |
|**hotelId** | **Integer** | Only return blocks for this specific hotel. |  [optional] |
|**ratePlanCodes** | **List&lt;String&gt;** | Return all blocks that have related the specified comma-separated rate plans. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Return all blocks where the block status is one of the specified values. |  [optional] |
|**to** | **OffsetDateTime** | Return all blocks where the block&#39;s last_departure is less than specified date. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| CANCELLED | &quot;Cancelled&quot; |
| TENTATIVE | &quot;Tentative&quot; |
| DEFINITE | &quot;Definite&quot; |



