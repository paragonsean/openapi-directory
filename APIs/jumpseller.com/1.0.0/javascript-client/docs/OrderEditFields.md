# JumpsellerApi.OrderEditFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalFields** | [**[OrderAdditionalFields]**](OrderAdditionalFields.md) | Array of additional fields for the given Order | [optional] 
**additionalInformation** | **String** | Additional information for the given Order | [optional] 
**shipmentStatus** | **String** | Status of the Order Shipping | [optional] 
**status** | **String** | Status of the Order | [optional] 
**trackingCompany** | **String** | Shipping Company used for the given Order | [optional] 
**trackingNumber** | **String** | Shipping Tracking Number used for the given Order | [optional] 
**trackingUrl** | **String** | URL to check delivery information for the given Order | [optional] 



## Enum: ShipmentStatusEnum


* `requested` (value: `"requested"`)

* `in_transit` (value: `"in_transit"`)

* `delivered` (value: `"delivered"`)

* `failed` (value: `"failed"`)

* `pickup_available` (value: `"pickup_available"`)





## Enum: StatusEnum


* `Abandoned` (value: `"Abandoned"`)

* `Canceled` (value: `"Canceled"`)

* `Pending Payment` (value: `"Pending Payment"`)

* `Paid` (value: `"Paid"`)




