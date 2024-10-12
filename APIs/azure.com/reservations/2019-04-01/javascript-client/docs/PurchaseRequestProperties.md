# AzureReservation.PurchaseRequestProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedScopeType** | [**AppliedScopeType**](AppliedScopeType.md) |  | [optional] 
**appliedScopes** | **[String]** | List of the subscriptions that the benefit will be applied. Do not specify if AppliedScopeType is Shared. | [optional] 
**billingPlan** | [**ReservationBillingPlan**](ReservationBillingPlan.md) |  | [optional] 
**billingScopeId** | **String** | Subscription that will be charged for purchasing Reservation | [optional] 
**displayName** | **String** | Friendly name of the Reservation | [optional] 
**quantity** | **Number** | Quantity of the SKUs that are part of the Reservation. Must be greater than zero. | [optional] 
**renew** | **Boolean** | Setting this to true will automatically purchase a new reservation on the expiration date time. | [optional] [default to false]
**reservedResourceProperties** | [**PurchaseRequestPropertiesReservedResourceProperties**](PurchaseRequestPropertiesReservedResourceProperties.md) |  | [optional] 
**reservedResourceType** | [**ReservedResourceType**](ReservedResourceType.md) |  | [optional] 
**term** | [**ReservationTerm**](ReservationTerm.md) |  | [optional] 


