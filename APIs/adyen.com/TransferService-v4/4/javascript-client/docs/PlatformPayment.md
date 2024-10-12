# TransfersApi.PlatformPayment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modificationMerchantReference** | **String** | The capture&#39;s merchant reference included in the transfer. | [optional] 
**modificationPspReference** | **String** | The capture reference included in the transfer. | [optional] 
**paymentMerchantReference** | **String** | The payment&#39;s merchant reference included in the transfer. | [optional] 
**platformPaymentType** | **String** | The type of the related split. | [optional] 
**pspPaymentReference** | **String** | The payment reference included in the transfer. | [optional] 
**type** | **String** | **platformPayment** | [optional] [default to &#39;platformPayment&#39;]



## Enum: PlatformPaymentTypeEnum


* `AcquiringFees` (value: `"AcquiringFees"`)

* `AdyenCommission` (value: `"AdyenCommission"`)

* `AdyenFees` (value: `"AdyenFees"`)

* `AdyenMarkup` (value: `"AdyenMarkup"`)

* `BalanceAccount` (value: `"BalanceAccount"`)

* `Commission` (value: `"Commission"`)

* `Default` (value: `"Default"`)

* `Interchange` (value: `"Interchange"`)

* `PaymentFee` (value: `"PaymentFee"`)

* `Remainder` (value: `"Remainder"`)

* `SchemeFee` (value: `"SchemeFee"`)

* `TopUp` (value: `"TopUp"`)

* `VAT` (value: `"VAT"`)





## Enum: TypeEnum


* `platformPayment` (value: `"platformPayment"`)




