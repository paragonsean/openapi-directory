

# Order


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **UUID** |  |  |
|**numberOfLineItems** | **Integer** |  |  |
|**orderNumber** | **String** |  |  |
|**orderStatus** | [**OrderStatusEnum**](#OrderStatusEnum) |  |  |
|**links** | [**PaginationLinks**](PaginationLinks.md) |  |  [optional] |
|**orderLineItems** | [**List&lt;OrderLineItem&gt;**](OrderLineItem.md) |  |  [optional] |



## Enum: OrderStatusEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;Active&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| COMPLETED | &quot;Completed&quot; |



