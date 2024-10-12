# PaymentsResellerSubscriptionApi.GoogleCloudPaymentsResellerSubscriptionV1Promotion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicableProducts** | **[String]** | Output only. The product ids this promotion can be applied to. | [optional] [readonly] 
**endTime** | **String** | Optional. Specifies the end time (exclusive) of the period that the promotion is available in. If unset, the promotion is available indefinitely. | [optional] 
**freeTrialDuration** | [**GoogleCloudPaymentsResellerSubscriptionV1Duration**](GoogleCloudPaymentsResellerSubscriptionV1Duration.md) |  | [optional] 
**introductoryPricingDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails**](GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails.md) |  | [optional] 
**name** | **String** | Identifier. Response only. Resource name of the subscription promotion. It will have the format of \&quot;partners/{partner_id}/promotion/{promotion_id}\&quot; | [optional] 
**promotionType** | **String** | Output only. Output Only. Specifies the type of the promotion. | [optional] [readonly] 
**regionCodes** | **[String]** | Output only. 2-letter ISO region code where the promotion is available in. Ex. \&quot;US\&quot; Please refers to: https://en.wikipedia.org/wiki/ISO_3166-1 | [optional] [readonly] 
**startTime** | **String** | Optional. Specifies the start time (inclusive) of the period that the promotion is available in. | [optional] 
**titles** | [**[GoogleTypeLocalizedText]**](GoogleTypeLocalizedText.md) | Output only. Localized human readable name of the promotion. | [optional] [readonly] 



## Enum: PromotionTypeEnum


* `UNSPECIFIED` (value: `"PROMOTION_TYPE_UNSPECIFIED"`)

* `FREE_TRIAL` (value: `"PROMOTION_TYPE_FREE_TRIAL"`)

* `INTRODUCTORY_PRICING` (value: `"PROMOTION_TYPE_INTRODUCTORY_PRICING"`)




