# GooglePlayAndroidDeveloperApi.SubscriptionPurchaseV2

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acknowledgementState** | **String** | The acknowledgement state of the subscription. | [optional] 
**canceledStateContext** | [**CanceledStateContext**](CanceledStateContext.md) |  | [optional] 
**externalAccountIdentifiers** | [**ExternalAccountIdentifiers**](ExternalAccountIdentifiers.md) |  | [optional] 
**kind** | **String** | This kind represents a SubscriptionPurchaseV2 object in the androidpublisher service. | [optional] 
**latestOrderId** | **String** | The order id of the latest order associated with the purchase of the subscription. For autoRenewing subscription, this is the order id of signup order if it is not renewed yet, or the last recurring order id (success, pending, or declined order). For prepaid subscription, this is the order id associated with the queried purchase token. | [optional] 
**lineItems** | [**[SubscriptionPurchaseLineItem]**](SubscriptionPurchaseLineItem.md) | Item-level info for a subscription purchase. The items in the same purchase should be either all with AutoRenewingPlan or all with PrepaidPlan. | [optional] 
**linkedPurchaseToken** | **String** | The purchase token of the old subscription if this subscription is one of the following: * Re-signup of a canceled but non-lapsed subscription * Upgrade/downgrade from a previous subscription. * Convert from prepaid to auto renewing subscription. * Convert from an auto renewing subscription to prepaid. * Topup a prepaid subscription. | [optional] 
**pausedStateContext** | [**PausedStateContext**](PausedStateContext.md) |  | [optional] 
**regionCode** | **String** | ISO 3166-1 alpha-2 billing country/region code of the user at the time the subscription was granted. | [optional] 
**startTime** | **String** | Time at which the subscription was granted. Not set for pending subscriptions (subscription was created but awaiting payment during signup). | [optional] 
**subscribeWithGoogleInfo** | [**SubscribeWithGoogleInfo**](SubscribeWithGoogleInfo.md) |  | [optional] 
**subscriptionState** | **String** | The current state of the subscription. | [optional] 
**testPurchase** | **Object** | Whether this subscription purchase is a test purchase. | [optional] 



## Enum: AcknowledgementStateEnum


* `UNSPECIFIED` (value: `"ACKNOWLEDGEMENT_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"ACKNOWLEDGEMENT_STATE_PENDING"`)

* `ACKNOWLEDGED` (value: `"ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED"`)





## Enum: SubscriptionStateEnum


* `UNSPECIFIED` (value: `"SUBSCRIPTION_STATE_UNSPECIFIED"`)

* `PENDING` (value: `"SUBSCRIPTION_STATE_PENDING"`)

* `ACTIVE` (value: `"SUBSCRIPTION_STATE_ACTIVE"`)

* `PAUSED` (value: `"SUBSCRIPTION_STATE_PAUSED"`)

* `IN_GRACE_PERIOD` (value: `"SUBSCRIPTION_STATE_IN_GRACE_PERIOD"`)

* `ON_HOLD` (value: `"SUBSCRIPTION_STATE_ON_HOLD"`)

* `CANCELED` (value: `"SUBSCRIPTION_STATE_CANCELED"`)

* `EXPIRED` (value: `"SUBSCRIPTION_STATE_EXPIRED"`)




