

# GetPaymentResult


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**links** | [**PaymentLinks**](PaymentLinks.md) |  |  [optional] |
|**amount** | **Long** |  |  [optional] |
|**cardBrand** | **String** | Card Brand |  [optional] [readonly] |
|**cardDetails** | [**CardDetails**](CardDetails.md) |  |  [optional] |
|**corporateCardSurcharge** | **Long** |  |  [optional] [readonly] |
|**createdDate** | **String** |  |  [optional] [readonly] |
|**delayedCapture** | **Boolean** | delayed capture flag |  [optional] [readonly] |
|**description** | **String** |  |  [optional] |
|**email** | **String** |  |  [optional] |
|**fee** | **Long** | processing fee taken by the GOV.UK Pay platform, in pence. Only available depending on payment service provider |  [optional] [readonly] |
|**language** | [**LanguageEnum**](#LanguageEnum) |  |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** |  |  [optional] |
|**moto** | **Boolean** | Mail Order / Telephone Order (MOTO) payment flag |  [optional] [readonly] |
|**netAmount** | **Long** | amount including all surcharges and less all fees, in pence. Only available depending on payment service provider |  [optional] [readonly] |
|**paymentId** | **String** |  |  [optional] [readonly] |
|**paymentProvider** | **String** |  |  [optional] [readonly] |
|**providerId** | **String** |  |  [optional] [readonly] |
|**reference** | **String** |  |  [optional] |
|**refundSummary** | [**RefundSummary**](RefundSummary.md) |  |  [optional] |
|**returnUrl** | **String** |  |  [optional] [readonly] |
|**settlementSummary** | [**PaymentSettlementSummary**](PaymentSettlementSummary.md) |  |  [optional] |
|**state** | [**PaymentState**](PaymentState.md) |  |  [optional] |
|**totalAmount** | **Long** |  |  [optional] [readonly] |



## Enum: LanguageEnum

| Name | Value |
|---- | -----|
| EN | &quot;en&quot; |
| CY | &quot;cy&quot; |



