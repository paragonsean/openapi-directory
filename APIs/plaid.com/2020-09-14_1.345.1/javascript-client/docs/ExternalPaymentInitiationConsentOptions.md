# ThePlaidApi.ExternalPaymentInitiationConsentOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bacs** | [**PaymentInitiationOptionalRestrictionBacs**](PaymentInitiationOptionalRestrictionBacs.md) |  | [optional] 
**iban** | **String** | The International Bank Account Number (IBAN) for the payer&#39;s account. Where possible, the end user will be able to set up payment consent using only the specified bank account if provided. | [optional] 
**requestRefundDetails** | **Boolean** | When &#x60;true&#x60;, Plaid will attempt to request refund details from the payee&#39;s financial institution.  Support varies between financial institutions and will not always be available.  If refund details could be retrieved, they will be available in the &#x60;/payment_initiation/payment/get&#x60; response. | [optional] 


