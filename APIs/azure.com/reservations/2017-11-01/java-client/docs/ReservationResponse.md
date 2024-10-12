

# ReservationResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**etag** | **Integer** |  |  [optional] |
|**id** | **String** | Identifier of the reservation |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | Resource Provider type to be reserved. |  [optional] |
|**location** | **Location** |  |  [optional] |
|**name** | **String** | Name of the reservation |  [optional] [readonly] |
|**properties** | [**ReservationProperties**](ReservationProperties.md) |  |  [optional] |
|**sku** | [**SkuName**](SkuName.md) |  |  [optional] |
|**type** | **String** | Type of resource. \&quot;Microsoft.Capacity/reservationOrders/reservations\&quot; |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| MICROSOFT_COMPUTE | &quot;Microsoft.Compute&quot; |



