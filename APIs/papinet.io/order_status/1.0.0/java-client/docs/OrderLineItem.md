

# OrderLineItem


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changeable** | **Boolean** |  |  [optional] |
|**id** | **UUID** |  |  |
|**orderLineItemNumber** | **BigDecimal** |  |  |
|**orderLineItemStatus** | [**OrderLineItemStatusEnum**](#OrderLineItemStatusEnum) |  |  |
|**quantities** | [**List&lt;OrderLineItemQuantitiesInner&gt;**](OrderLineItemQuantitiesInner.md) |  |  [optional] |



## Enum: OrderLineItemStatusEnum

| Name | Value |
|---- | -----|
| CANCELLED | &quot;Cancelled&quot; |
| COMPLETED | &quot;Completed&quot; |
| CONFIRMED | &quot;Confirmed&quot; |
| PENDING | &quot;Pending&quot; |
| PRODUCTION_COMPLETED | &quot;ProductionCompleted&quot; |
| SHIPMENT_COMPLETED | &quot;ShipmentCompleted&quot; |



