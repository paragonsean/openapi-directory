# PaymentsResellerSubscriptionApi.GoogleCloudPaymentsResellerSubscriptionV1Subscription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancellationDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionCancellationDetails.md) |  | [optional] 
**createTime** | **String** | Output only. System generated timestamp when the subscription is created. UTC timezone. | [optional] [readonly] 
**cycleEndTime** | **String** | Output only. The time at which the subscription is expected to be extended, in ISO 8061 format. UTC timezone. For example: \&quot;2019-08-31T17:28:54.564Z\&quot; | [optional] [readonly] 
**endUserEntitled** | **Boolean** | Output only. Indicates if the subscription is entitled to the end user. | [optional] [readonly] 
**freeTrialEndTime** | **String** | Output only. End of the free trial period, in ISO 8061 format. For example, \&quot;2019-08-31T17:28:54.564Z\&quot;. It will be set the same as createTime if no free trial promotion is specified. | [optional] [readonly] 
**lineItems** | [**[GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem]**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem.md) | Required. The line items of the subscription. | [optional] 
**name** | **String** | Identifier. Resource name of the subscription. It will have the format of \&quot;partners/{partner_id}/subscriptions/{subscription_id}\&quot;. This is available for authorizeAddon, but otherwise is response only. | [optional] 
**partnerUserToken** | **String** | Required. Identifier of the end-user in partner’s system. The value is restricted to 63 ASCII characters at the maximum. | [optional] 
**processingState** | **String** | Output only. Describes the processing state of the subscription. See more details at [the lifecycle of a subscription](/payments/reseller/subscription/reference/index/Receive.Notifications#payments-subscription-lifecycle). | [optional] [readonly] 
**products** | **[String]** | Optional. Deprecated: consider using &#x60;line_items&#x60; as the input. Required. Resource name that identifies the purchased products. The format will be &#39;partners/{partner_id}/products/{product_id}&#39;. | [optional] 
**promotionSpecs** | [**[GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec]**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec.md) | Optional. Subscription-level promotions. Only free trial is supported on this level. It determines the first renewal time of the subscription to be the end of the free trial period. Specify the promotion resource name only when used as input. | [optional] 
**promotions** | **[String]** | Optional. Deprecated: consider using the top-level &#x60;promotion_specs&#x60; as the input. Optional. Resource name that identifies one or more promotions that can be applied on the product. A typical promotion for a subscription is Free trial. The format will be &#39;partners/{partner_id}/promotions/{promotion_id}&#39;. | [optional] 
**redirectUri** | **String** | Output only. The place where partners should redirect the end-user to after creation. This field might also be populated when creation failed. However, Partners should always prepare a default URL to redirect the user in case this field is empty. | [optional] [readonly] 
**renewalTime** | **String** | Output only. The time at which the subscription is expected to be renewed by Google - a new charge will be incurred and the service entitlement will be renewed. A non-immediate cancellation will take place at this time too, before which, the service entitlement for the end user will remain valid. UTC timezone in ISO 8061 format. For example: \&quot;2019-08-31T17:28:54.564Z\&quot; | [optional] [readonly] 
**serviceLocation** | [**GoogleCloudPaymentsResellerSubscriptionV1Location**](GoogleCloudPaymentsResellerSubscriptionV1Location.md) |  | [optional] 
**state** | **String** | Output only. Describes the state of the subscription. See more details at [the lifecycle of a subscription](/payments/reseller/subscription/reference/index/Receive.Notifications#payments-subscription-lifecycle). | [optional] [readonly] 
**updateTime** | **String** | Output only. System generated timestamp when the subscription is most recently updated. UTC timezone. | [optional] [readonly] 
**upgradeDowngradeDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionUpgradeDowngradeDetails.md) |  | [optional] 



## Enum: ProcessingStateEnum


* `UNSPECIFIED` (value: `"PROCESSING_STATE_UNSPECIFIED"`)

* `CANCELLING` (value: `"PROCESSING_STATE_CANCELLING"`)

* `RECURRING` (value: `"PROCESSING_STATE_RECURRING"`)





## Enum: StateEnum


* `UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATED` (value: `"STATE_CREATED"`)

* `ACTIVE` (value: `"STATE_ACTIVE"`)

* `CANCELLED` (value: `"STATE_CANCELLED"`)

* `IN_GRACE_PERIOD` (value: `"STATE_IN_GRACE_PERIOD"`)

* `CANCEL_AT_END_OF_CYCLE` (value: `"STATE_CANCEL_AT_END_OF_CYCLE"`)

* `SUSPENDED` (value: `"STATE_SUSPENDED"`)




