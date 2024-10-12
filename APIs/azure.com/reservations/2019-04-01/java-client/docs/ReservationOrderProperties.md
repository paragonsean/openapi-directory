

# ReservationOrderProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingPlan** | **ReservationBillingPlan** |  |  [optional] |
|**createdDateTime** | **OffsetDateTime** | This is the DateTime when the reservation was created. |  [optional] |
|**displayName** | **String** | Friendly name for user to easily identified the reservation. |  [optional] |
|**expiryDate** | **LocalDate** | This is the date when the Reservation will expire. |  [optional] |
|**originalQuantity** | **Integer** | Quantity of the SKUs that are part of the Reservation. Must be greater than zero. |  [optional] |
|**planInformation** | [**ReservationOrderBillingPlanInformation**](ReservationOrderBillingPlanInformation.md) |  |  [optional] |
|**provisioningState** | **String** | Current state of the reservation. |  [optional] |
|**requestDateTime** | **OffsetDateTime** | This is the DateTime when the reservation was initially requested for purchase. |  [optional] |
|**reservations** | [**List&lt;ReservationResponse&gt;**](ReservationResponse.md) |  |  [optional] |
|**term** | **ReservationTerm** |  |  [optional] |



