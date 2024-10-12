# GovUkPayApi.GetPaymentResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaymentLinks**](PaymentLinks.md) |  | [optional] 
**amount** | **Number** |  | [optional] 
**cardBrand** | **String** | Card Brand | [optional] [readonly] 
**cardDetails** | [**CardDetails**](CardDetails.md) |  | [optional] 
**corporateCardSurcharge** | **Number** |  | [optional] [readonly] 
**createdDate** | **String** |  | [optional] [readonly] 
**delayedCapture** | **Boolean** | delayed capture flag | [optional] [readonly] 
**description** | **String** |  | [optional] 
**email** | **String** |  | [optional] 
**fee** | **Number** | processing fee taken by the GOV.UK Pay platform, in pence. Only available depending on payment service provider | [optional] [readonly] 
**language** | **String** |  | [optional] 
**metadata** | **{String: String}** |  | [optional] 
**moto** | **Boolean** | Mail Order / Telephone Order (MOTO) payment flag | [optional] [readonly] 
**netAmount** | **Number** | amount including all surcharges and less all fees, in pence. Only available depending on payment service provider | [optional] [readonly] 
**paymentId** | **String** |  | [optional] [readonly] 
**paymentProvider** | **String** |  | [optional] [readonly] 
**providerId** | **String** |  | [optional] [readonly] 
**reference** | **String** |  | [optional] 
**refundSummary** | [**RefundSummary**](RefundSummary.md) |  | [optional] 
**returnUrl** | **String** |  | [optional] [readonly] 
**settlementSummary** | [**PaymentSettlementSummary**](PaymentSettlementSummary.md) |  | [optional] 
**state** | [**PaymentState**](PaymentState.md) |  | [optional] 
**totalAmount** | **Number** |  | [optional] [readonly] 



## Enum: LanguageEnum


* `en` (value: `"en"`)

* `cy` (value: `"cy"`)




