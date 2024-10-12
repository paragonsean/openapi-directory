# AzureReservation.ReservationOrderProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingPlan** | [**ReservationBillingPlan**](ReservationBillingPlan.md) |  | [optional] 
**createdDateTime** | **Date** | This is the DateTime when the reservation was created. | [optional] 
**displayName** | **String** | Friendly name for user to easily identified the reservation. | [optional] 
**expiryDate** | **Date** | This is the date when the Reservation will expire. | [optional] 
**originalQuantity** | **Number** | Quantity of the SKUs that are part of the Reservation. Must be greater than zero. | [optional] 
**planInformation** | [**ReservationOrderBillingPlanInformation**](ReservationOrderBillingPlanInformation.md) |  | [optional] 
**provisioningState** | **String** | Current state of the reservation. | [optional] 
**requestDateTime** | **Date** | This is the DateTime when the reservation was initially requested for purchase. | [optional] 
**reservations** | [**[ReservationResponse]**](ReservationResponse.md) |  | [optional] 
**term** | [**ReservationTerm**](ReservationTerm.md) |  | [optional] 


