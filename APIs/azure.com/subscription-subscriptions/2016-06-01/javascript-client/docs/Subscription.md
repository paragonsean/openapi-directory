# SubscriptionClient.Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**authorizationSource** | **String** | The authorization source of the request. Valid values are one or more combinations of Legacy, RoleBased, Bypassed, Direct and Management. For example, &#39;Legacy, RoleBased&#39;. | [optional] 
**displayName** | **String** | The subscription display name. | [optional] [readonly] 
**id** | **String** | The fully qualified ID for the subscription. For example, /subscriptions/00000000-0000-0000-0000-000000000000. | [optional] [readonly] 
**state** | **String** | The subscription state. Possible values are Enabled, Warned, PastDue, Disabled, and Deleted. | [optional] [readonly] 
**subscriptionId** | **String** | The subscription ID. | [optional] [readonly] 
**subscriptionPolicies** | [**SubscriptionPolicies**](SubscriptionPolicies.md) |  | [optional] 



## Enum: StateEnum


* `Enabled` (value: `"Enabled"`)

* `Warned` (value: `"Warned"`)

* `PastDue` (value: `"PastDue"`)

* `Disabled` (value: `"Disabled"`)

* `Deleted` (value: `"Deleted"`)




