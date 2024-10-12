# AzureReservation.PatchProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appliedScopeType** | [**AppliedScopeType**](AppliedScopeType.md) |  | [optional] 
**appliedScopes** | **[String]** | List of the subscriptions that the benefit will be applied. Do not specify if AppliedScopeType is Shared. | [optional] 
**instanceFlexibility** | [**InstanceFlexibility**](InstanceFlexibility.md) |  | [optional] 
**name** | **String** | Name of the Reservation | [optional] 
**renew** | **Boolean** | Setting this to true will automatically purchase a new reservation on the expiration date time. | [optional] [default to false]
**renewProperties** | [**PatchPropertiesRenewProperties**](PatchPropertiesRenewProperties.md) |  | [optional] 


