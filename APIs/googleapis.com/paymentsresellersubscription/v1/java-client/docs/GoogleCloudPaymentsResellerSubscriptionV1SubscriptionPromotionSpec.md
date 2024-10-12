

# GoogleCloudPaymentsResellerSubscriptionV1SubscriptionPromotionSpec

Describes the spec for one promotion.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**freeTrialDuration** | [**GoogleCloudPaymentsResellerSubscriptionV1Duration**](GoogleCloudPaymentsResellerSubscriptionV1Duration.md) |  |  [optional] |
|**introductoryPricingDetails** | [**GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails**](GoogleCloudPaymentsResellerSubscriptionV1PromotionIntroductoryPricingDetails.md) |  |  [optional] |
|**promotion** | **String** | Required. Promotion resource name that identifies a promotion. The format is &#39;partners/{partner_id}/promotions/{promotion_id}&#39;. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. The type of the promotion for the spec. |  [optional] [readonly] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PROMOTION_TYPE_UNSPECIFIED&quot; |
| FREE_TRIAL | &quot;PROMOTION_TYPE_FREE_TRIAL&quot; |
| INTRODUCTORY_PRICING | &quot;PROMOTION_TYPE_INTRODUCTORY_PRICING&quot; |



