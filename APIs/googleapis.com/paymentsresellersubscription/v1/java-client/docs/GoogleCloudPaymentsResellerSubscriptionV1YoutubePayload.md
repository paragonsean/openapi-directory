

# GoogleCloudPaymentsResellerSubscriptionV1YoutubePayload

Payload specific to Youtube products.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessEndTime** | **String** | Output only. The access expiration time for this line item. |  [optional] [readonly] |
|**partnerEligibilityIds** | **List&lt;String&gt;** | The list of eligibility_ids which are applicable for the line item. |  [optional] |
|**partnerPlanType** | [**PartnerPlanTypeEnum**](#PartnerPlanTypeEnum) | Optional. Specifies the plan type offered to the end user by the partner. |  [optional] |



## Enum: PartnerPlanTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PARTNER_PLAN_TYPE_UNSPECIFIED&quot; |
| STANDALONE | &quot;PARTNER_PLAN_TYPE_STANDALONE&quot; |
| HARD_BUNDLE | &quot;PARTNER_PLAN_TYPE_HARD_BUNDLE&quot; |
| SOFT_BUNDLE | &quot;PARTNER_PLAN_TYPE_SOFT_BUNDLE&quot; |



