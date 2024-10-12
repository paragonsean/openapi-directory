

# ReservationProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedScopeType** | **AppliedScopeType** |  |  [optional] |
|**appliedScopes** | **List&lt;String&gt;** | List of the subscriptions that the benefit will be applied. Do not specify if AppliedScopeType is Shared. |  [optional] |
|**displayName** | **String** | Friendly name for user to easily identify the reservation |  [optional] |
|**effectiveDateTime** | **OffsetDateTime** | DateTime of the Reservation starting when this version is effective from. |  [optional] |
|**expiryDate** | **LocalDate** | This is the date when the Reservation will expire. |  [optional] |
|**extendedStatusInfo** | [**ExtendedStatusInfo**](ExtendedStatusInfo.md) |  |  [optional] |
|**instanceFlexibility** | **InstanceFlexibility** |  |  [optional] |
|**lastUpdatedDateTime** | **OffsetDateTime** | DateTime of the last time the Reservation was updated. |  [optional] [readonly] |
|**mergeProperties** | [**ReservationMergeProperties**](ReservationMergeProperties.md) |  |  [optional] |
|**provisioningState** | **String** | Current state of the reservation. |  [optional] |
|**quantity** | **Integer** | Quantity of the SKUs that are part of the Reservation. |  [optional] |
|**reservedResourceType** | **ReservedResourceType** |  |  [optional] |
|**skuDescription** | **String** | Description of the SKU in english. |  [optional] |
|**splitProperties** | [**ReservationSplitProperties**](ReservationSplitProperties.md) |  |  [optional] |



