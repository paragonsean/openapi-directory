# ThePlaidApi.PaymentInitiationMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximumPaymentAmount** | **{String: String}** | A mapping of currency to maximum payment amount (denominated in the smallest unit of currency) supported by the institution.  Example: &#x60;{\&quot;GBP\&quot;: \&quot;10000\&quot;}&#x60;  | 
**standingOrderMetadata** | [**PaymentInitiationStandingOrderMetadata**](PaymentInitiationStandingOrderMetadata.md) |  | 
**supportsInternationalPayments** | **Boolean** | Indicates whether the institution supports payments from a different country. | 
**supportsRefundDetails** | **Boolean** | Indicates whether the institution supports returning refund details when initiating a payment. | 
**supportsSepaInstant** | **Boolean** | Indicates whether the institution supports SEPA Instant payments. | 


