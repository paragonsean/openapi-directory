# JumpsellerApi.FulfillmentEditFields

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expectedArrivalFrom** | **String** | First date expected for the fulfillment to arrive at customer place | [optional] 
**expectedArrivalTo** | **String** | Last date expected for the fulfillment to arrive at customer place | [optional] 
**externalId** | **String** | Unique identifier of the Fulfillment used by the tracking company | [optional] 
**orderId** | **String** | Order associated with the fulfillment | [optional] 
**serviceType** | **String** | Type of Service requested to the tracking company | [optional] 
**shipmentStatus** | **String** | Status of the Fulfillment | [optional] 
**trackingCompany** | **String** | Tracking company responsible for the fulfillment | [optional] 
**trackingNumber** | **String** | Tracking Number associated with the fulfillment | [optional] 
**type** | **String** | Type of fulfillment Service used | [optional] 



## Enum: ShipmentStatusEnum


* `requested` (value: `"requested"`)

* `in_transit` (value: `"in_transit"`)

* `delivered` (value: `"delivered"`)

* `failed` (value: `"failed"`)





## Enum: TypeEnum


* `manual` (value: `"manual"`)

* `shipit` (value: `"shipit"`)

* `chilexpress` (value: `"chilexpress"`)

* `ctt` (value: `"ctt"`)

* `correos_chile` (value: `"correos_chile"`)

* `dhl` (value: `"dhl"`)

* `servientrega` (value: `"servientrega"`)

* `starken` (value: `"starken"`)

* `bluexpress` (value: `"bluexpress"`)




