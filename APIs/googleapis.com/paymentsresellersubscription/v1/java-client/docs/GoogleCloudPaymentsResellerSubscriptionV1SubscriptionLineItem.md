

# GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem

Individual line item definition of a subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | [**GoogleCloudPaymentsResellerSubscriptionV1Amount**](GoogleCloudPaymentsResellerSubscriptionV1Amount.md) |  |  [optional] |
|**bundleDetails** | [**SubscriptionLineItemBundleDetails**](SubscriptionLineItemBundleDetails.md) |  |  [optional] |
|**description** | **String** | Output only. Description of this line item. |  [optional] [readonly] |
|**finiteBillingCycleDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails**](GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails.md) |  |  [optional] |
|**lineItemFreeTrialEndTime** | **String** | Output only. The free trial end time will be populated after the line item is successfully processed. End time of the line item free trial period, in ISO 8061 format. For example, \&quot;2019-08-31T17:28:54.564Z\&quot;. It will be set the same as createTime if no free trial promotion is specified. |  [optional] [readonly] |
|**lineItemIndex** | **Integer** | Output only. A unique index of the subscription line item. |  [optional] [readonly] |
|**lineItemPromotionSpecs** | [**List&lt;GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec&gt;**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec.md) | Optional. The promotions applied on the line item. It can be: - a free trial promotion, which overrides the subscription-level free trial promotion. - an introductory pricing promotion. When used as input in Create or Provision API, specify its resource name only. |  [optional] |
|**oneTimeRecurrenceDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetails**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetails.md) |  |  [optional] |
|**product** | **String** | Required. Product resource name that identifies one the line item The format is &#39;partners/{partner_id}/products/{product_id}&#39;. |  [optional] |
|**productPayload** | [**GoogleCloudPaymentsResellerSubscriptionV1ProductPayload**](GoogleCloudPaymentsResellerSubscriptionV1ProductPayload.md) |  |  [optional] |
|**recurrenceType** | [**RecurrenceTypeEnum**](#RecurrenceTypeEnum) | Output only. The recurrence type of the line item. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the line item. |  [optional] [readonly] |



## Enum: RecurrenceTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LINE_ITEM_RECURRENCE_TYPE_UNSPECIFIED&quot; |
| PERIODIC | &quot;LINE_ITEM_RECURRENCE_TYPE_PERIODIC&quot; |
| ONE_TIME | &quot;LINE_ITEM_RECURRENCE_TYPE_ONE_TIME&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;LINE_ITEM_STATE_UNSPECIFIED&quot; |
| ACTIVE | &quot;LINE_ITEM_STATE_ACTIVE&quot; |
| INACTIVE | &quot;LINE_ITEM_STATE_INACTIVE&quot; |
| NEW | &quot;LINE_ITEM_STATE_NEW&quot; |
| ACTIVATING | &quot;LINE_ITEM_STATE_ACTIVATING&quot; |
| DEACTIVATING | &quot;LINE_ITEM_STATE_DEACTIVATING&quot; |
| WAITING_TO_DEACTIVATE | &quot;LINE_ITEM_STATE_WAITING_TO_DEACTIVATE&quot; |
| OFF_CYCLE_CHARGING | &quot;LINE_ITEM_STATE_OFF_CYCLE_CHARGING&quot; |



