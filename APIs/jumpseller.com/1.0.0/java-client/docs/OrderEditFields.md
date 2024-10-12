

# OrderEditFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalFields** | [**List&lt;OrderAdditionalFields&gt;**](OrderAdditionalFields.md) | Array of additional fields for the given Order |  [optional] |
|**additionalInformation** | **String** | Additional information for the given Order |  [optional] |
|**shipmentStatus** | [**ShipmentStatusEnum**](#ShipmentStatusEnum) | Status of the Order Shipping |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of the Order |  [optional] |
|**trackingCompany** | **String** | Shipping Company used for the given Order |  [optional] |
|**trackingNumber** | **String** | Shipping Tracking Number used for the given Order |  [optional] |
|**trackingUrl** | **String** | URL to check delivery information for the given Order |  [optional] |



## Enum: ShipmentStatusEnum

| Name | Value |
|---- | -----|
| REQUESTED | &quot;requested&quot; |
| IN_TRANSIT | &quot;in_transit&quot; |
| DELIVERED | &quot;delivered&quot; |
| FAILED | &quot;failed&quot; |
| PICKUP_AVAILABLE | &quot;pickup_available&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ABANDONED | &quot;Abandoned&quot; |
| CANCELED | &quot;Canceled&quot; |
| PENDING_PAYMENT | &quot;Pending Payment&quot; |
| PAID | &quot;Paid&quot; |



