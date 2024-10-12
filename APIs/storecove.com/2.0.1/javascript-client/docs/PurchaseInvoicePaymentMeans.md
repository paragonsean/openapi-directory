# StorecoveApi.PurchaseInvoicePaymentMeans

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | The account number to which to transfer. | [optional] 
**branchCode** | **String** | The code identifying the bank branch. May contain a BIC/SWIFT or something appropriate for the payment method, such as \&quot;NPP\&quot; for type NppPaymentMean. | [optional] 
**holder** | **String** | The account holder name to which to transfer. | [optional] 
**mandate** | **String** | The mandate, used only for type DirectDebitPaymentMean. | [optional] 
**network** | **String** | The payment network. Used only for type CardPaymentType. | [optional] 
**paymentId** | **String** | The payment id to use when making the payment. The invoice sender will use this to match the received funds to the invoice. | [optional] 
**type** | **String** | The type of payment means. Which type are returned is determined by the &amp;pmv&#x3D; query parameter. For details see documentation for that field. | [optional] 



## Enum: TypeEnum


* `BankPaymentMean` (value: `"BankPaymentMean"`)

* `DirectDebitPaymentMean` (value: `"DirectDebitPaymentMean"`)

* `CardPaymentMean` (value: `"CardPaymentMean"`)

* `NppPaymentMean` (value: `"NppPaymentMean"`)

* `SeBankGiroPaymentMean` (value: `"SeBankGiroPaymentMean"`)

* `SePlusgiroPaymentMean` (value: `"SePlusgiroPaymentMean"`)

* `SgCardPaymentMean` (value: `"SgCardPaymentMean"`)

* `SgGiroPaymentMean` (value: `"SgGiroPaymentMean"`)

* `SgPaynowPaymentMean` (value: `"SgPaynowPaymentMean"`)

* `CreditTransferPaymentMean` (value: `"CreditTransferPaymentMean"`)

* `CreditCardPaymentMean` (value: `"CreditCardPaymentMean"`)

* `SeBankgiroPaymentMean` (value: `"SeBankgiroPaymentMean"`)

* `AunzNppPayidPaymentMean` (value: `"AunzNppPayidPaymentMean"`)

* `OnlinePaymentServicePaymentMean` (value: `"OnlinePaymentServicePaymentMean"`)

* `StandingAgreementPaymentMean` (value: `"StandingAgreementPaymentMean"`)

* `AunzNppPaytoPaymentMean` (value: `"AunzNppPaytoPaymentMean"`)

* `AunzBpayPaymentMean` (value: `"AunzBpayPaymentMean"`)

* `AunzPostbillpayPaymentMean` (value: `"AunzPostbillpayPaymentMean"`)

* `AunzUriPaymentMean` (value: `"AunzUriPaymentMean"`)




