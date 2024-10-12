

# OrderFulfillmentsInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** |  |  [optional] |
|**pickupDetails** | [**OrderFulfillmentsInnerPickupDetails**](OrderFulfillmentsInnerPickupDetails.md) |  |  [optional] |
|**shipmentDetails** | **Object** |  |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | The state of the fulfillment. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| PROPOSED | &quot;proposed&quot; |
| RESERVED | &quot;reserved&quot; |
| PREPARED | &quot;prepared&quot; |
| COMPLETED | &quot;completed&quot; |
| CANCELLED | &quot;cancelled&quot; |
| FAILED | &quot;failed&quot; |
| OTHER | &quot;other&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| PICKUP | &quot;pickup&quot; |
| SHIPMENT | &quot;shipment&quot; |



