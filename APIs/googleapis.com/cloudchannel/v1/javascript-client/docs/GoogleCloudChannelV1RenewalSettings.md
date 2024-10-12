# CloudChannelApi.GoogleCloudChannelV1RenewalSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enableRenewal** | **Boolean** | If false, the plan will be completed at the end date. | [optional] 
**paymentCycle** | [**GoogleCloudChannelV1Period**](GoogleCloudChannelV1Period.md) |  | [optional] 
**paymentPlan** | **String** | Describes how a reseller will be billed. | [optional] 
**resizeUnitCount** | **Boolean** | If true and enable_renewal &#x3D; true, the unit (for example seats or licenses) will be set to the number of active units at renewal time. | [optional] 



## Enum: PaymentPlanEnum


* `PAYMENT_PLAN_UNSPECIFIED` (value: `"PAYMENT_PLAN_UNSPECIFIED"`)

* `COMMITMENT` (value: `"COMMITMENT"`)

* `FLEXIBLE` (value: `"FLEXIBLE"`)

* `FREE` (value: `"FREE"`)

* `TRIAL` (value: `"TRIAL"`)

* `OFFLINE` (value: `"OFFLINE"`)




