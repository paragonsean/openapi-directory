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
**instanceFlexibility** | [**InstanceFlexibility**](InstanceFlexibility.md) |  | [optional] 
**lastUpdatedDateTime** | **Date** | DateTime of the last time the Reservation was updated. | [optional] [readonly] 
**mergeProperties** | [**ReservationMergeProperties**](ReservationMergeProperties.md) |  | [optional] 
**provisioningState** | **String** | Current state of the reservation. | [optional] 
**quantity** | **Number** | Quantity of the SKUs that are part of the Reservation. | [optional] 
**reservedResourceType** | [**ReservedResourceType**](ReservedResourceType.md) |  | [optional] 
**skuDescription** | **String** | Description of the SKU in english. | [optional] 
**splitProperties** | [**ReservationSplitProperties**](ReservationSplitProperties.md) |  | [optional] 


