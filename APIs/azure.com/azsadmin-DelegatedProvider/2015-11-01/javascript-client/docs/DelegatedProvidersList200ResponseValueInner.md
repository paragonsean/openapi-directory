# SubscriptionsManagementClient.DelegatedProvidersList200ResponseValueInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delegatedProviderSubscriptionId** | **String** | Parent DelegatedProvider subscription identifier. | [optional] 
**displayName** | **String** | Subscription name. | [optional] 
**externalReferenceId** | **String** | External reference identifier. | [optional] 
**id** | **String** | Fully qualified identifier. | [optional] 
**offerId** | **String** | Identifier of the offer under the scope of a delegated provider. | [optional] 
**owner** | **String** | Subscription owner. | [optional] 
**routingResourceManagerType** | **String** | Resource manager type. | [optional] 
**state** | **String** | Subscription notification state. | [optional] 
**subscriptionId** | **String** | Subscription identifier. | [optional] 
**tenantId** | **String** | Directory tenant identifier. | [optional] 



## Enum: RoutingResourceManagerTypeEnum


* `Default` (value: `"Default"`)

* `Admin` (value: `"Admin"`)





## Enum: StateEnum


* `NotDefined` (value: `"NotDefined"`)

* `Enabled` (value: `"Enabled"`)

* `Warned` (value: `"Warned"`)

* `PastDue` (value: `"PastDue"`)

* `Disabled` (value: `"Disabled"`)

* `Deleted` (value: `"Deleted"`)

* `Deleting` (value: `"Deleting"`)

* `PartiallyDeleted` (value: `"PartiallyDeleted"`)




