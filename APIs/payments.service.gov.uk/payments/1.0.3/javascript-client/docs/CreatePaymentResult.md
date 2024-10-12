# GovUkPayApi.CreatePaymentResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**PaymentLinks**](PaymentLinks.md) |  | [optional] 
**amount** | **Number** | The amount in pence. | [optional] 
**cardDetails** | [**CardDetails**](CardDetails.md) |  | [optional] 
**createdDate** | **String** | The date you created the payment. | [optional] 
**delayedCapture** | **Boolean** | Whether to [delay capturing](https://docs.payments.service.gov.uk/optional_features/delayed_capture/) this payment. | [optional] 
**description** | **String** | The human-readable description you gave the payment. | [optional] 
**email** | **String** | The email address of your user. | [optional] 
**language** | **String** | Which language your users will see on the payment pages when they make a payment. | [optional] 
**metadata** | **{String: String}** | [Custom metadata](https://docs.payments.service.gov.uk/optional_features/custom_metadata/) you added to the payment. | [optional] 
**moto** | **Boolean** | Mail Order / Telephone Order (MOTO) payment flag. | [optional] 
**paymentId** | **String** | The unique identifier of the payment. | [optional] 
**paymentProvider** | **String** |  | [optional] 
**providerId** | **String** | The reference number the payment gateway associated with the payment. | [optional] 
**reference** | **String** | The reference number you associated with this payment. | [optional] 
**refundSummary** | [**RefundSummary**](RefundSummary.md) |  | [optional] 
**returnUrl** | **String** | An HTTPS URL on your site that your user will be sent back to once they have completed their payment attempt on GOV.UK Pay. | [optional] 
**settlementSummary** | [**PaymentSettlementSummary**](PaymentSettlementSummary.md) |  | [optional] 
**state** | [**PaymentState**](PaymentState.md) |  | [optional] 



## Enum: LanguageEnum


* `en` (value: `"en"`)

* `cy` (value: `"cy"`)




