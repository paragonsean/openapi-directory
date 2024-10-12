# CloudChannelApi.GoogleCloudChannelV1alpha1RenewalSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disableCommitment** | **Boolean** | If true, disables commitment-based offer on renewal and switches to flexible or pay as you go. Deprecated: Use &#x60;payment_plan&#x60; instead. | [optional] 
**enableRenewal** | **Boolean** | If false, the plan will be completed at the end date. | [optional] 
**paymentCycle** | [**GoogleCloudChannelV1alpha1Period**](GoogleCloudChannelV1alpha1Period.md) |  | [optional] 
**paymentOption** | **String** | Set if enable_renewal&#x3D;true. Deprecated: Use &#x60;payment_cycle&#x60; instead. | [optional] 
**paymentPlan** | **String** | Describes how a reseller will be billed. | [optional] 
**resizeUnitCount** | **Boolean** | If true and enable_renewal &#x3D; true, the unit (for example seats or licenses) will be set to the number of active units at renewal time. | [optional] 
**scheduledRenewalOffer** | **String** | Output only. The offer resource name that the entitlement will renew on at the end date. Takes the form: accounts/{account_id}/offers/{offer_id}. | [optional] [readonly] 



## Enum: PaymentOptionEnum


* `PAYMENT_OPTION_UNSPECIFIED` (value: `"PAYMENT_OPTION_UNSPECIFIED"`)

* `ANNUAL` (value: `"ANNUAL"`)

* `MONTHLY` (value: `"MONTHLY"`)





## Enum: PaymentPlanEnum


* `PAYMENT_PLAN_UNSPECIFIED` (value: `"PAYMENT_PLAN_UNSPECIFIED"`)

* `COMMITMENT` (value: `"COMMITMENT"`)

* `FLEXIBLE` (value: `"FLEXIBLE"`)

* `FREE` (value: `"FREE"`)

* `TRIAL` (value: `"TRIAL"`)

* `OFFLINE` (value: `"OFFLINE"`)




