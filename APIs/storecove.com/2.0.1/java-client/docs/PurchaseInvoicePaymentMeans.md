

# PurchaseInvoicePaymentMeans


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**account** | **String** | The account number to which to transfer. |  [optional] |
|**branchCode** | **String** | The code identifying the bank branch. May contain a BIC/SWIFT or something appropriate for the payment method, such as \&quot;NPP\&quot; for type NppPaymentMean. |  [optional] |
|**holder** | **String** | The account holder name to which to transfer. |  [optional] |
|**mandate** | **String** | The mandate, used only for type DirectDebitPaymentMean. |  [optional] |
|**network** | **String** | The payment network. Used only for type CardPaymentType. |  [optional] |
|**paymentId** | **String** | The payment id to use when making the payment. The invoice sender will use this to match the received funds to the invoice. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of payment means. Which type are returned is determined by the &amp;pmv&#x3D; query parameter. For details see documentation for that field. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BANK_PAYMENT_MEAN | &quot;BankPaymentMean&quot; |
| DIRECT_DEBIT_PAYMENT_MEAN | &quot;DirectDebitPaymentMean&quot; |
| CARD_PAYMENT_MEAN | &quot;CardPaymentMean&quot; |
| NPP_PAYMENT_MEAN | &quot;NppPaymentMean&quot; |
| SE_BANK_GIRO_PAYMENT_MEAN | &quot;SeBankGiroPaymentMean&quot; |
| SE_PLUSGIRO_PAYMENT_MEAN | &quot;SePlusgiroPaymentMean&quot; |
| SG_CARD_PAYMENT_MEAN | &quot;SgCardPaymentMean&quot; |
| SG_GIRO_PAYMENT_MEAN | &quot;SgGiroPaymentMean&quot; |
| SG_PAYNOW_PAYMENT_MEAN | &quot;SgPaynowPaymentMean&quot; |
| CREDIT_TRANSFER_PAYMENT_MEAN | &quot;CreditTransferPaymentMean&quot; |
| CREDIT_CARD_PAYMENT_MEAN | &quot;CreditCardPaymentMean&quot; |
| SE_BANKGIRO_PAYMENT_MEAN | &quot;SeBankgiroPaymentMean&quot; |
| AUNZ_NPP_PAYID_PAYMENT_MEAN | &quot;AunzNppPayidPaymentMean&quot; |
| ONLINE_PAYMENT_SERVICE_PAYMENT_MEAN | &quot;OnlinePaymentServicePaymentMean&quot; |
| STANDING_AGREEMENT_PAYMENT_MEAN | &quot;StandingAgreementPaymentMean&quot; |
| AUNZ_NPP_PAYTO_PAYMENT_MEAN | &quot;AunzNppPaytoPaymentMean&quot; |
| AUNZ_BPAY_PAYMENT_MEAN | &quot;AunzBpayPaymentMean&quot; |
| AUNZ_POSTBILLPAY_PAYMENT_MEAN | &quot;AunzPostbillpayPaymentMean&quot; |
| AUNZ_URI_PAYMENT_MEAN | &quot;AunzUriPaymentMean&quot; |



