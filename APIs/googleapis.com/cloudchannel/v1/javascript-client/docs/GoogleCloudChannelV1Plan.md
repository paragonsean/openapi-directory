# CloudChannelApi.GoogleCloudChannelV1Plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billingAccount** | **String** | Reseller Billing account to charge after an offer transaction. Only present for Google Cloud offers. | [optional] 
**paymentCycle** | [**GoogleCloudChannelV1Period**](GoogleCloudChannelV1Period.md) |  | [optional] 
**paymentPlan** | **String** | Describes how a reseller will be billed. | [optional] 
**paymentType** | **String** | Specifies when the payment needs to happen. | [optional] 
**trialPeriod** | [**GoogleCloudChannelV1Period**](GoogleCloudChannelV1Period.md) |  | [optional] 



## Enum: PaymentPlanEnum


* `PAYMENT_PLAN_UNSPECIFIED` (value: `"PAYMENT_PLAN_UNSPECIFIED"`)

* `COMMITMENT` (value: `"COMMITMENT"`)

* `FLEXIBLE` (value: `"FLEXIBLE"`)

* `FREE` (value: `"FREE"`)

* `TRIAL` (value: `"TRIAL"`)

* `OFFLINE` (value: `"OFFLINE"`)





## Enum: PaymentTypeEnum


* `PAYMENT_TYPE_UNSPECIFIED` (value: `"PAYMENT_TYPE_UNSPECIFIED"`)

* `PREPAY` (value: `"PREPAY"`)

* `POSTPAY` (value: `"POSTPAY"`)




