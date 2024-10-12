# AzureReservation.ReservationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedScopeType** | [**AppliedScopeType**](AppliedScopeType.md) |  | [optional] 
**appliedScopes** | **[String]** | List of the subscriptions that the benefit will be applied. Do not specify if AppliedScopeType is Shared. | [optional] 
**displayName** | **String** | Friendly name for user to easily identify the reservation | [optional] 
**effectiveDateTime** | **Date** | DateTime of the Reservation starting when this version is effective from. | [optional] 
**expiryDate** | **Date** | This is the date when the Reservation will expire. | [optional] 
**extendedStatusInfo** | [**ExtendedStatusInfo**](ExtendedStatusInfo.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** | DateTime of the last time the Reservation was updated. | [optional] [readonly] 
**mergeProperties** | [**ReservationMergeProperties**](ReservationMergeProperties.md) |  | [optional] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 
**quantity** | **Number** | Quantity of the SKUs that are part of the Reservation. | [optional] 
**splitProperties** | [**ReservationSplitProperties**](ReservationSplitProperties.md) |  | [optional] 


