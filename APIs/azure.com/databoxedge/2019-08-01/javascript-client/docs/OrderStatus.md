# DataBoxEdgeManagementClient.OrderStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalOrderDetails** | **{String: String}** | Dictionary to hold generic information which is not stored  by the already existing properties | [optional] [readonly] 
**comments** | **String** | Comments related to this status change. | [optional] 
**status** | **String** | Status of the order as per the allowed status types. | 
**updateDateTime** | **Date** | Time of status update. | [optional] [readonly] 



## Enum: StatusEnum


* `Untracked` (value: `"Untracked"`)

* `AwaitingFulfilment` (value: `"AwaitingFulfilment"`)

* `AwaitingPreparation` (value: `"AwaitingPreparation"`)

* `AwaitingShipment` (value: `"AwaitingShipment"`)

* `Shipped` (value: `"Shipped"`)

* `Arriving` (value: `"Arriving"`)

* `Delivered` (value: `"Delivered"`)

* `ReplacementRequested` (value: `"ReplacementRequested"`)

* `LostDevice` (value: `"LostDevice"`)

* `Declined` (value: `"Declined"`)

* `ReturnInitiated` (value: `"ReturnInitiated"`)

* `AwaitingReturnShipment` (value: `"AwaitingReturnShipment"`)

* `ShippedBack` (value: `"ShippedBack"`)

* `CollectedAtMicrosoft` (value: `"CollectedAtMicrosoft"`)




