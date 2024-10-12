

# BasePlan

A single base plan for a subscription.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoRenewingBasePlanType** | [**AutoRenewingBasePlanType**](AutoRenewingBasePlanType.md) |  |  [optional] |
|**basePlanId** | **String** | Required. Immutable. The unique identifier of this base plan. Must be unique within the subscription, and conform with RFC-1034. That is, this ID can only contain lower-case letters (a-z), numbers (0-9), and hyphens (-), and be at most 63 characters. |  [optional] |
|**offerTags** | [**List&lt;OfferTag&gt;**](OfferTag.md) | List of up to 20 custom tags specified for this base plan, and returned to the app through the billing library. Subscription offers for this base plan will also receive these offer tags in the billing library. |  [optional] |
|**otherRegionsConfig** | [**OtherRegionsBasePlanConfig**](OtherRegionsBasePlanConfig.md) |  |  [optional] |
|**prepaidBasePlanType** | [**PrepaidBasePlanType**](PrepaidBasePlanType.md) |  |  [optional] |
|**regionalConfigs** | [**List&lt;RegionalBasePlanConfig&gt;**](RegionalBasePlanConfig.md) | Region-specific information for this base plan. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The state of the base plan, i.e. whether it&#39;s active. Draft and inactive base plans can be activated or deleted. Active base plans can be made inactive. Inactive base plans can be canceled. This field cannot be changed by updating the resource. Use the dedicated endpoints instead. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| DRAFT | &quot;DRAFT&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| INACTIVE | &quot;INACTIVE&quot; |



