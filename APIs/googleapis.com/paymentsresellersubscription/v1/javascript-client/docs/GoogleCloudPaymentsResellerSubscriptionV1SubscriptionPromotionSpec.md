# PaymentsResellerSubscriptionApi.GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**freeTrialDuration** | [**GoogleCloudPaymentsResellerSubscriptionV1Duration**](GoogleCloudPaymentsResellerSubscriptionV1Duration.md) |  | [optional] 
**introductoryPricingDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails**](GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails.md) |  | [optional] 
**promotion** | **String** | Required. Promotion resource name that identifies a promotion. The format is &#39;partners/{partner_id}/promotions/{promotion_id}&#39;. | [optional] 
**type** | **String** | Output only. The type of the promotion for the spec. | [optional] [readonly] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"PROMOTION_TYPE_UNSPECIFIED"`)

* `FREE_TRIAL` (value: `"PROMOTION_TYPE_FREE_TRIAL"`)

* `INTRODUCTORY_PRICING` (value: `"PROMOTION_TYPE_INTRODUCTORY_PRICING"`)




