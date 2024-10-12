

# GoogleCloudChannelV1RenewalSettings

Renewal settings for renewable Offers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableRenewal** | **Boolean** | If false, the plan will be completed at the end date. |  [optional] |
|**paymentCycle** | [**GoogleCloudChannelV1Period**](GoogleCloudChannelV1Period.md) |  |  [optional] |
|**paymentPlan** | [**PaymentPlanEnum**](#PaymentPlanEnum) | Describes how a reseller will be billed. |  [optional] |
|**resizeUnitCount** | **Boolean** | If true and enable_renewal &#x3D; true, the unit (for example seats or licenses) will be set to the number of active units at renewal time. |  [optional] |



## Enum: PaymentPlanEnum

| Name | Value |
|---- | -----|
| PAYMENT_PLAN_UNSPECIFIED | &quot;PAYMENT_PLAN_UNSPECIFIED&quot; |
| COMMITMENT | &quot;COMMITMENT&quot; |
| FLEXIBLE | &quot;FLEXIBLE&quot; |
| FREE | &quot;FREE&quot; |
| TRIAL | &quot;TRIAL&quot; |
| OFFLINE | &quot;OFFLINE&quot; |



