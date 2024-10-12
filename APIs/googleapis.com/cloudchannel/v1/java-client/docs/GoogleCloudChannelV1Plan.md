

# GoogleCloudChannelV1Plan

The payment plan for the Offer. Describes how to make a payment.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**billingAccount** | **String** | Reseller Billing account to charge after an offer transaction. Only present for Google Cloud offers. |  [optional] |
|**paymentCycle** | [**GoogleCloudChannelV1Period**](GoogleCloudChannelV1Period.md) |  |  [optional] |
|**paymentPlan** | [**PaymentPlanEnum**](#PaymentPlanEnum) | Describes how a reseller will be billed. |  [optional] |
|**paymentType** | [**PaymentTypeEnum**](#PaymentTypeEnum) | Specifies when the payment needs to happen. |  [optional] |
|**trialPeriod** | [**GoogleCloudChannelV1Period**](GoogleCloudChannelV1Period.md) |  |  [optional] |



## Enum: PaymentPlanEnum

| Name | Value |
|---- | -----|
| PAYMENT_PLAN_UNSPECIFIED | &quot;PAYMENT_PLAN_UNSPECIFIED&quot; |
| COMMITMENT | &quot;COMMITMENT&quot; |
| FLEXIBLE | &quot;FLEXIBLE&quot; |
| FREE | &quot;FREE&quot; |
| TRIAL | &quot;TRIAL&quot; |
| OFFLINE | &quot;OFFLINE&quot; |



## Enum: PaymentTypeEnum

| Name | Value |
|---- | -----|
| PAYMENT_TYPE_UNSPECIFIED | &quot;PAYMENT_TYPE_UNSPECIFIED&quot; |
| PREPAY | &quot;PREPAY&quot; |
| POSTPAY | &quot;POSTPAY&quot; |



