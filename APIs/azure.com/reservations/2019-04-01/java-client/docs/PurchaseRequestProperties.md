

# PurchaseRequestProperties


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**appliedScopeType** | **AppliedScopeType** |  |  [optional] |
|**appliedScopes** | **List&lt;String&gt;** | List of the subscriptions that the benefit will be applied. Do not specify if AppliedScopeType is Shared. |  [optional] |
|**billingPlan** | **ReservationBillingPlan** |  |  [optional] |
|**billingScopeId** | **String** | Subscription that will be charged for purchasing Reservation |  [optional] |
|**displayName** | **String** | Friendly name of the Reservation |  [optional] |
|**quantity** | **Integer** | Quantity of the SKUs that are part of the Reservation. Must be greater than zero. |  [optional] |
|**renew** | **Boolean** | Setting this to true will automatically purchase a new reservation on the expiration date time. |  [optional] |
|**reservedResourceProperties** | [**PurchaseRequestPropertiesReservedResourceProperties**](PurchaseRequestPropertiesReservedResourceProperties.md) |  |  [optional] |
|**reservedResourceType** | **ReservedResourceType** |  |  [optional] |
|**term** | **ReservationTerm** |  |  [optional] |



