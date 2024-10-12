# AzureReservation.ReservationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedScopeType** | [**AppliedScopeType**](AppliedScopeType.md) |  | [optional] 
**appliedScopes** | **[String]** | List of the subscriptions that the benefit will be applied. Do not specify if AppliedScopeType is Shared. | [optional] 
**billingPlan** | [**ReservationBillingPlan**](ReservationBillingPlan.md) |  | [optional] 
**billingScopeId** | **String** | Subscription that will be charged for purchasing Reservation | [optional] 
**displayName** | **String** | Friendly name for user to easily identify the reservation | [optional] 
**effectiveDateTime** | **Date** | DateTime of the Reservation starting when this version is effective from. | [optional] 
**expiryDate** | **Date** | This is the date when the Reservation will expire. | [optional] 
**extendedStatusInfo** | [**ExtendedStatusInfo**](ExtendedStatusInfo.md) |  | [optional] 
**instanceFlexibility** | [**InstanceFlexibility**](InstanceFlexibility.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** | DateTime of the last time the Reservation was updated. | [optional] [readonly] 
**mergeProperties** | [**ReservationMergeProperties**](ReservationMergeProperties.md) |  | [optional] 
**provisioningState** | **String** | Current state of the reservation. | [optional] 
**quantity** | **Number** | Quantity of the SKUs that are part of the Reservation. Must be greater than zero. | [optional] 
**renew** | **Boolean** | Setting this to true will automatically purchase a new reservation on the expiration date time. | [optional] [default to false]
**renewDestination** | **String** | Reservation Id of the reservation which is purchased because of renew. Format of the resource Id is /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}. | [optional] 
**renewProperties** | [**RenewPropertiesResponse**](RenewPropertiesResponse.md) |  | [optional] 
**renewSource** | **String** | Reservation Id of the reservation from which this reservation is renewed. Format of the resource Id is /providers/Microsoft.Capacity/reservationOrders/{reservationOrderId}/reservations/{reservationId}. | [optional] 
**reservedResourceType** | [**ReservedResourceType**](ReservedResourceType.md) |  | [optional] 
**skuDescription** | **String** | Description of the SKU in english. | [optional] 
**splitProperties** | [**ReservationSplitProperties**](ReservationSplitProperties.md) |  | [optional] 
**term** | [**ReservationTerm**](ReservationTerm.md) |  | [optional] 


