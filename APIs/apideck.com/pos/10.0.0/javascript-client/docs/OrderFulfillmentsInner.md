# PosApi.OrderFulfillmentsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** |  | [optional] 
**pickupDetails** | [**OrderFulfillmentsInnerPickupDetails**](OrderFulfillmentsInnerPickupDetails.md) |  | [optional] 
**shipmentDetails** | **Object** |  | [optional] 
**status** | **String** | The state of the fulfillment. | [optional] 
**type** | **String** |  | [optional] 



## Enum: StatusEnum


* `proposed` (value: `"proposed"`)

* `reserved` (value: `"reserved"`)

* `prepared` (value: `"prepared"`)

* `completed` (value: `"completed"`)

* `cancelled` (value: `"cancelled"`)

* `failed` (value: `"failed"`)

* `other` (value: `"other"`)





## Enum: TypeEnum


* `pickup` (value: `"pickup"`)

* `shipment` (value: `"shipment"`)




