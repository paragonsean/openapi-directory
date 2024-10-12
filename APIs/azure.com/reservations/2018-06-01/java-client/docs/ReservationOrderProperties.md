

# ReservationOrderProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDateTime** | **OffsetDateTime** | This is the DateTime when the reservation was created. |  [optional] |
|**displayName** | **String** | Friendly name for user to easily identified the reservation. |  [optional] |
|**expiryDate** | **LocalDate** | This is the date when the Reservation will expire. |  [optional] |
|**originalQuantity** | **Integer** | Total Quantity of the SKUs purchased in the Reservation. |  [optional] |
|**provisioningState** | **String** | Current state of the reservation. |  [optional] |
|**requestDateTime** | **OffsetDateTime** | This is the DateTime when the reservation was initially requested for purchase. |  [optional] |
|**reservations** | [**List&lt;ReservationResponse&gt;**](ReservationResponse.md) |  |  [optional] |
|**term** | **ReservationTerm** |  |  [optional] |



