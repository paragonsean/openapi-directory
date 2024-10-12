

# PaymentResponseV3


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** |  |  [optional] |
|**accountNumber** | **String** | The account number for the account which will receive the payment. |  [optional] |
|**countryCode** | **String** | The country code of the payment channel. |  [optional] |
|**events** | [**List&lt;PaymentEventResponseV3&gt;**](PaymentEventResponseV3.md) |  |  |
|**filenameReference** | **String** | ACH file payment was submitted in, if applicable |  [optional] |
|**fundingStatus** | **String** | The funding status of the payment. One of the following values: [FUNDED, INSTRUCTED, UNFUNDED |  |
|**iban** | **String** | The iban for the payment. |  [optional] |
|**individualIdentificationNumber** | **String** | Individual Identification Number assigned to the payment in the ACH file, if applicable |  [optional] |
|**invertedRate** | **Float** | The inverted FX rate for the payment, if FX was involved. **Note** that (depending on the role of the caller) this information may not be displayed |  [optional] |
|**payeeId** | **UUID** | The id of the paymeee |  |
|**paymentAmount** | **Integer** | The amount which the payee will receive |  |
|**paymentChannelId** | **String** |  |  [optional] |
|**paymentChannelName** | **String** |  |  [optional] |
|**paymentCurrency** | **String** | ISO 3 character currency code |  [optional] |
|**paymentId** | **UUID** | The id of the payment |  |
|**paymentMemo** | **String** | The payment memo set by the payor |  [optional] |
|**paymentScheme** | **String** |  |  [optional] |
|**payorId** | **UUID** | The id of the payor |  |
|**payorName** | **String** | The name of the payor |  [optional] |
|**payorPaymentId** | **String** |  |  [optional] |
|**quoteId** | **UUID** | The quote Id used for the FX |  |
|**railsBatchId** | **String** |  |  [optional] |
|**railsId** | **String** | The rails ID. Default value is RAILS ID UNAVAILABLE when not populated. |  |
|**railsPaymentId** | **String** |  |  [optional] |
|**rate** | **Float** | The FX rate for the payment, if FX was involved. **Note** that (depending on the role of the caller) this information may not be displayed |  [optional] |
|**rejectionReason** | **String** |  |  [optional] |
|**remoteId** | **String** | The remote id by which the payor refers to the payee. Only populated once payment is confirmed |  [optional] |
|**returnCost** | **Integer** | The return cost if a returned payment. |  [optional] |
|**returnReason** | **String** |  |  [optional] |
|**routingNumber** | **String** | The routing number for the payment. |  [optional] |
|**sourceAccountId** | **UUID** | The id of the source account from which the payment was taken |  |
|**sourceAccountName** | **String** | The name of the source account from which the payment was taken |  [optional] |
|**sourceAmount** | **Integer** | The source amount for the payment (amount debited to make the payment) |  [optional] |
|**sourceCurrency** | **String** | ISO 3 character currency code |  [optional] |
|**status** | **String** | Current status of the payment. One of the following values: ACCEPTED, AWAITING_FUNDS, FUNDED, UNFUNDED, BANK_PAYMENT_REQUESTED, REJECTED, ACCEPTED_BY_RAILS, CONFIRMED, FAILED, WITHDRAWN |  |
|**submittedDateTime** | **OffsetDateTime** |  |  |
|**traceNumber** | **String** | Trace Number assigned to the payment in the ACH file, if applicable |  [optional] |



