

# GoogleCloudChannelV1alpha1RenewalSettings

Renewal settings for renewable Offers.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disableCommitment** | **Boolean** | If true, disables commitment-based offer on renewal and switches to flexible or pay as you go. Deprecated: Use &#x60;payment_plan&#x60; instead. |  [optional] |
|**enableRenewal** | **Boolean** | If false, the plan will be completed at the end date. |  [optional] |
|**paymentCycle** | [**GoogleCloudChannelV1alpha1Period**](GoogleCloudChannelV1alpha1Period.md) |  |  [optional] |
|**paymentOption** | [**PaymentOptionEnum**](#PaymentOptionEnum) | Set if enable_renewal&#x3D;true. Deprecated: Use &#x60;payment_cycle&#x60; instead. |  [optional] |
|**paymentPlan** | [**PaymentPlanEnum**](#PaymentPlanEnum) | Describes how a reseller will be billed. |  [optional] |
|**resizeUnitCount** | **Boolean** | If true and enable_renewal &#x3D; true, the unit (for example seats or licenses) will be set to the number of active units at renewal time. |  [optional] |
|**scheduledRenewalOffer** | **String** | Output only. The offer resource name that the entitlement will renew on at the end date. Takes the form: accounts/{account_id}/offers/{offer_id}. |  [optional] [readonly] |



## Enum: PaymentOptionEnum

| Name | Value |
|---- | -----|
| PAYMENT_OPTION_UNSPECIFIED | &quot;PAYMENT_OPTION_UNSPECIFIED&quot; |
| ANNUAL | &quot;ANNUAL&quot; |
| MONTHLY | &quot;MONTHLY&quot; |



## Enum: PaymentPlanEnum

| Name | Value |
|---- | -----|
| PAYMENT_PLAN_UNSPECIFIED | &quot;PAYMENT_PLAN_UNSPECIFIED&quot; |
| COMMITMENT | &quot;COMMITMENT&quot; |
| FLEXIBLE | &quot;FLEXIBLE&quot; |
| FREE | &quot;FREE&quot; |
| TRIAL | &quot;TRIAL&quot; |
| OFFLINE | &quot;OFFLINE&quot; |



