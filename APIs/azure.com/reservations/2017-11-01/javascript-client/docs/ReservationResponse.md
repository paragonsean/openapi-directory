# AzureReservation.ReservationResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**etag** | **Number** |  | [optional] 
**id** | **String** | Identifier of the reservation | [optional] [readonly] 
**kind** | **String** | Resource Provider type to be reserved. | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**name** | **String** | Name of the reservation | [optional] [readonly] 
**properties** | [**ReservationProperties**](ReservationProperties.md) |  | [optional] 
**sku** | [**SkuName**](SkuName.md) |  | [optional] 
**type** | **String** | Type of resource. \&quot;Microsoft.Capacity/reservationOrders/reservations\&quot; | [optional] [readonly] 



## Enum: KindEnum


* `Microsoft.Compute` (value: `"Microsoft.Compute"`)




