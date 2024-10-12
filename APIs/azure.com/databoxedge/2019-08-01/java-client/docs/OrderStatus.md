

# OrderStatus

Represents a single status change.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalOrderDetails** | **Map&lt;String, String&gt;** | Dictionary to hold generic information which is not stored  by the already existing properties |  [optional] [readonly] |
|**comments** | **String** | Comments related to this status change. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the order as per the allowed status types. |  |
|**updateDateTime** | **OffsetDateTime** | Time of status update. |  [optional] [readonly] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| UNTRACKED | &quot;Untracked&quot; |
| AWAITING_FULFILMENT | &quot;AwaitingFulfilment&quot; |
| AWAITING_PREPARATION | &quot;AwaitingPreparation&quot; |
| AWAITING_SHIPMENT | &quot;AwaitingShipment&quot; |
| SHIPPED | &quot;Shipped&quot; |
| ARRIVING | &quot;Arriving&quot; |
| DELIVERED | &quot;Delivered&quot; |
| REPLACEMENT_REQUESTED | &quot;ReplacementRequested&quot; |
| LOST_DEVICE | &quot;LostDevice&quot; |
| DECLINED | &quot;Declined&quot; |
| RETURN_INITIATED | &quot;ReturnInitiated&quot; |
| AWAITING_RETURN_SHIPMENT | &quot;AwaitingReturnShipment&quot; |
| SHIPPED_BACK | &quot;ShippedBack&quot; |
| COLLECTED_AT_MICROSOFT | &quot;CollectedAtMicrosoft&quot; |



