

# FulfillmentCreateFields


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**expectedArrivalFrom** | **String** | First date expected for the fulfillment to arrive at customer place |  [optional] |
|**expectedArrivalTo** | **String** | Last date expected for the fulfillment to arrive at customer place |  [optional] |
|**externalId** | **String** | Unique identifier of the Fulfillment used by the tracking company |  [optional] |
|**orderId** | **String** | Order associated with the fulfillment |  [optional] |
|**serviceType** | **String** | Type of Service requested to the tracking company |  [optional] |
|**shipmentStatus** | [**ShipmentStatusEnum**](#ShipmentStatusEnum) | Status of the Fulfillment |  [optional] |
|**trackingCompany** | **String** | Tracking company responsible for the fulfillment |  [optional] |
|**trackingNumber** | **String** | Tracking Number associated with the fulfillment |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of fulfillment Service used |  [optional] |



## Enum: ShipmentStatusEnum

| Name | Value |
|---- | -----|
| REQUESTED | &quot;requested&quot; |
| IN_TRANSIT | &quot;in_transit&quot; |
| DELIVERED | &quot;delivered&quot; |
| FAILED | &quot;failed&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| SHIPIT | &quot;shipit&quot; |
| CHILEXPRESS | &quot;chilexpress&quot; |
| CTT | &quot;ctt&quot; |
| CORREOS_CHILE | &quot;correos_chile&quot; |
| DHL | &quot;dhl&quot; |
| SERVIENTREGA | &quot;servientrega&quot; |
| STARKEN | &quot;starken&quot; |
| BLUEXPRESS | &quot;bluexpress&quot; |



