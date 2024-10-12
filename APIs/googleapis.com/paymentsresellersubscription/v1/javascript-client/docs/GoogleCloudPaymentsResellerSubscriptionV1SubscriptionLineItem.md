# PaymentsResellerSubscriptionApi.GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**GoogleCloudPaymentsResellerSubscriptionV1Amount**](GoogleCloudPaymentsResellerSubscriptionV1Amount.md) |  | [optional] 
**bundleDetails** | [**SubscriptionLineItemBundleDetails**](SubscriptionLineItemBundleDetails.md) |  | [optional] 
**description** | **String** | Output only. Description of this line item. | [optional] [readonly] 
**finiteBillingCycleDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails**](GoogleCloudPaymentsResellerSubscriptionV1FiniteBillingCycleDetails.md) |  | [optional] 
**lineItemFreeTrialEndTime** | **String** | Output only. The free trial end time will be populated after the line item is successfully processed. End time of the line item free trial period, in ISO 8061 format. For example, \&quot;2019-08-31T17:28:54.564Z\&quot;. It will be set the same as createTime if no free trial promotion is specified. | [optional] [readonly] 
**lineItemIndex** | **Number** | Output only. A unique index of the subscription line item. | [optional] [readonly] 
**lineItemPromotionSpecs** | [**[GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec]**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec.md) | Optional. The promotions applied on the line item. It can be: - a free trial promotion, which overrides the subscription-level free trial promotion. - an introductory pricing promotion. When used as input in Create or Provision API, specify its resource name only. | [optional] 
**oneTimeRecurrenceDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetails**](GoogleCloudPaymentsResellerSubscriptionV1SubscriptionLineItemOneTimeRecurrenceDetails.md) |  | [optional] 
**product** | **String** | Required. Product resource name that identifies one the line item The format is &#39;partners/{partner_id}/products/{product_id}&#39;. | [optional] 
**productPayload** | [**GoogleCloudPaymentsResellerSubscriptionV1ProductPayload**](GoogleCloudPaymentsResellerSubscriptionV1ProductPayload.md) |  | [optional] 
**recurrenceType** | **String** | Output only. The recurrence type of the line item. | [optional] [readonly] 
**state** | **String** | Output only. The state of the line item. | [optional] [readonly] 



## Enum: RecurrenceTypeEnum


* `UNSPECIFIED` (value: `"LINE_ITEM_RECURRENCE_TYPE_UNSPECIFIED"`)

* `PERIODIC` (value: `"LINE_ITEM_RECURRENCE_TYPE_PERIODIC"`)

* `ONE_TIME` (value: `"LINE_ITEM_RECURRENCE_TYPE_ONE_TIME"`)





## Enum: StateEnum


* `UNSPECIFIED` (value: `"LINE_ITEM_STATE_UNSPECIFIED"`)

* `ACTIVE` (value: `"LINE_ITEM_STATE_ACTIVE"`)

* `INACTIVE` (value: `"LINE_ITEM_STATE_INACTIVE"`)

* `NEW` (value: `"LINE_ITEM_STATE_NEW"`)

* `ACTIVATING` (value: `"LINE_ITEM_STATE_ACTIVATING"`)

* `DEACTIVATING` (value: `"LINE_ITEM_STATE_DEACTIVATING"`)

* `WAITING_TO_DEACTIVATE` (value: `"LINE_ITEM_STATE_WAITING_TO_DEACTIVATE"`)

* `OFF_CYCLE_CHARGING` (value: `"LINE_ITEM_STATE_OFF_CYCLE_CHARGING"`)




