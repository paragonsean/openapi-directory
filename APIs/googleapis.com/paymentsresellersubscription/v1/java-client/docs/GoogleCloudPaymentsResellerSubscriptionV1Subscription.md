

# GoogleCloudPaymentsResellerSubscriptionV1Subscription

A subscription serves as a central billing entity between an external partner and Google. The underlying Google services rely on the subscription state to grant or revoke the user's service entitlement. It's important to note that the subscription state may not always perfectly align with the user's service entitlement. For example, some Google services may continue providing access to the user until the current billing cycle ends, even if the subscription has been immediately canceled. However, other services may not do the same. To fully understand the specific details, please consult the relevant contract or product policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cancellationDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails.md) |  |  [optional] |
|**createTime** | **String** | Output only. System generated timestamp when the subscription is created. UTC timezone. |  [optional] [readonly] |
|**cycleEndTime** | **String** | Output only. The time at which the subscription is expected to be extended, in ISO 8061 format. UTC timezone. For example: \&quot;2019-08-31T17:28:54.564Z\&quot; |  [optional] [readonly] |
|**endUserEntitled** | **Boolean** | Output only. Indicates if the subscription is entitled to the end user. |  [optional] [readonly] |
|**freeTrialEndTime** | **String** | Output only. End of the free trial period, in ISO 8061 format. For example, \&quot;2019-08-31T17:28:54.564Z\&quot;. It will be set the same as createTime if no free trial promotion is specified. |  [optional] [readonly] |
|**lineItems** | [**List&lt;GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem&gt;**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem.md) | Required. The line items of the subscription. |  [optional] |
|**name** | **String** | Identifier. Resource name of the subscription. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot;. This is available for authorizeAddon, but otherwise is response only. |  [optional] |
|**partnerUserToken** | **String** | Required. Identifier of the end-user in partner’s system. The value is restricted to 63 ASCII characters at the maximum. |  [optional] |
|**processingState** | [**ProcessingStateEnum**](#ProcessingStateEnum) | Output only. Describes the processing state of the subscription. See more details at [the lifecycle of a subscription](/payments/reseller/subscription/reference/index/Receive.Notifications#payments-subscription-lifecycle). |  [optional] [readonly] |
|**products** | **List&lt;String&gt;** | Optional. Deprecated: consider using &#x60;line_items&#x60; as the input. Required. Resource name that identifies the purchased products. The format will be &#39;partners/{partner_id}/products/{product_id}&#39;. |  [optional] |
|**promotionSpecs** | [**List&lt;GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec&gt;**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec.md) | Optional. Subscription-level promotions. Only free trial is supported on this level. It determines the first renewal time of the subscription to be the end of the free trial period. Specify the promotion resource name only when used as input. |  [optional] |
|**promotions** | **List&lt;String&gt;** | Optional. Deprecated: consider using the top-level &#x60;promotion_specs&#x60; as the input. Optional. Resource name that identifies one or more promotions that can be applied on the product. A typical promotion for a subscription is Free trial. The format will be &#39;partners/{partner_id}/promotions/{promotion_id}&#39;. |  [optional] |
|**redirectUri** | **String** | Output only. The place where partners should redirect the end-user to after creation. This field might also be populated when creation failed. However, Partners should always prepare a default URL to redirect the user in case this field is empty. |  [optional] [readonly] |
|**renewalTime** | **String** | Output only. The time at which the subscription is expected to be renewed by Google - a new charge will be incurred and the service entitlement will be renewed. A non-immediate cancellation will take place at this time too, before which, the service entitlement for the end user will remain valid. UTC timezone in ISO 8061 format. For example: \&quot;2019-08-31T17:28:54.564Z\&quot; |  [optional] [readonly] |
|**serviceLocation** | [**GoogleCloudPaymentsResellerSubscriptionV1Location**](GoogleCloudPaymentsResellerSubscriptionV1Location.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Describes the state of the subscription. See more details at [the lifecycle of a subscription](/payments/reseller/subscription/reference/index/Receive.Notifications#payments-subscription-lifecycle). |  [optional] [readonly] |
|**updateTime** | **String** | Output only. System generated timestamp when the subscription is most recently updated. UTC timezone. |  [optional] [readonly] |
|**upgradeDowngradeDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails.md) |  |  [optional] |



## Enum: ProcessingStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PROCESSING_STATE_UNSPECIFIED&quot; |
| CANCELLING | &quot;PROCESSING_STATE_CANCELLING&quot; |
| RECURRING | &quot;PROCESSING_STATE_RECURRING&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATED | &quot;STATE_CREATED&quot; |
| ACTIVE | &quot;STATE_ACTIVE&quot; |
| CANCELLED | &quot;STATE_CANCELLED&quot; |
| IN_GRACE_PERIOD | &quot;STATE_IN_GRACE_PERIOD&quot; |
| CANCEL_AT_END_OF_CYCLE | &quot;STATE_CANCEL_AT_END_OF_CYCLE&quot; |
| SUSPENDED | &quot;STATE_SUSPENDED&quot; |



