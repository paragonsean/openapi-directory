

# SubscriptionPurchaseV2

Indicates the status of a user's subscription purchase.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acknowledgementState** | [**AcknowledgementStateEnum**](#AcknowledgementStateEnum) | The acknowledgement state of the subscription. |  [optional] |
|**canceledStateContext** | [**CanceledStateContext**](CanceledStateContext.md) |  |  [optional] |
|**externalAccountIdentifiers** | [**ExternalAccountIdentifiers**](ExternalAccountIdentifiers.md) |  |  [optional] |
|**kind** | **String** | This kind represents a SubscriptionPurchaseV2 object in the androidpublisher service. |  [optional] |
|**latestOrderId** | **String** | The order id of the latest order associated with the purchase of the subscription. For autoRenewing subscription, this is the order id of signup order if it is not renewed yet, or the last recurring order id (success, pending, or declined order). For prepaid subscription, this is the order id associated with the queried purchase token. |  [optional] |
|**lineItems** | [**List&lt;SubscriptionPurchaseLineItem&gt;**](SubscriptionPurchaseLineItem.md) | Item-level info for a subscription purchase. The items in the same purchase should be either all with AutoRenewingPlan or all with PrepaidPlan. |  [optional] |
|**linkedPurchaseToken** | **String** | The purchase token of the old subscription if this subscription is one of the following: * Re-signup of a canceled but non-lapsed subscription * Upgrade/downgrade from a previous subscription. * Convert from prepaid to auto renewing subscription. * Convert from an auto renewing subscription to prepaid. * Topup a prepaid subscription. |  [optional] |
|**pausedStateContext** | [**PausedStateContext**](PausedStateContext.md) |  |  [optional] |
|**regionCode** | **String** | ISO 3166-1 alpha-2 billing country/region code of the user at the time the subscription was granted. |  [optional] |
|**startTime** | **String** | Time at which the subscription was granted. Not set for pending subscriptions (subscription was created but awaiting payment during signup). |  [optional] |
|**subscribeWithGoogleInfo** | [**SubscribeWithGoogleInfo**](SubscribeWithGoogleInfo.md) |  |  [optional] |
|**subscriptionState** | [**SubscriptionStateEnum**](#SubscriptionStateEnum) | The current state of the subscription. |  [optional] |
|**testPurchase** | **Object** | Whether this subscription purchase is a test purchase. |  [optional] |



## Enum: AcknowledgementStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ACKNOWLEDGEMENT_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;ACKNOWLEDGEMENT_STATE_PENDING&quot; |
| ACKNOWLEDGED | &quot;ACKNOWLEDGEMENT_STATE_ACKNOWLEDGED&quot; |



## Enum: SubscriptionStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SUBSCRIPTION_STATE_UNSPECIFIED&quot; |
| PENDING | &quot;SUBSCRIPTION_STATE_PENDING&quot; |
| ACTIVE | &quot;SUBSCRIPTION_STATE_ACTIVE&quot; |
| PAUSED | &quot;SUBSCRIPTION_STATE_PAUSED&quot; |
| IN_GRACE_PERIOD | &quot;SUBSCRIPTION_STATE_IN_GRACE_PERIOD&quot; |
| ON_HOLD | &quot;SUBSCRIPTION_STATE_ON_HOLD&quot; |
| CANCELED | &quot;SUBSCRIPTION_STATE_CANCELED&quot; |
| EXPIRED | &quot;SUBSCRIPTION_STATE_EXPIRED&quot; |



