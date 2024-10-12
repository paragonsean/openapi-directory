# ThePlaidApi.PaymentInitiationPaymentGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustedReference** | **String** | The value of the reference sent to the bank after adjustment to pass bank validation rules. | [optional] 
**adjustedScheme** | [**PaymentScheme**](PaymentScheme.md) |  | [optional] 
**amount** | [**PaymentAmount**](PaymentAmount.md) |  | 
**amountRefunded** | [**PaymentAmountRefunded**](PaymentAmountRefunded.md) |  | [optional] 
**bacs** | [**SenderBACSNullable**](SenderBACSNullable.md) |  | 
**consentId** | **String** | The payment consent ID that this payment was initiated with. Is present only when payment was initiated using the payment consent. | [optional] 
**iban** | **String** | The International Bank Account Number (IBAN) for the sender, if specified in the &#x60;/payment_initiation/payment/create&#x60; call. | 
**lastStatusUpdate** | **Date** | The date and time of the last time the &#x60;status&#x60; was updated, in IS0 8601 format | 
**paymentId** | **String** | The ID of the payment. Like all Plaid identifiers, the &#x60;payment_id&#x60; is case sensitive. | 
**recipientId** | **String** | The ID of the recipient | 
**reference** | **String** | A reference for the payment. | 
**refundDetails** | [**ExternalPaymentRefundDetails**](ExternalPaymentRefundDetails.md) |  | [optional] 
**refundIds** | **[String]** | Refund IDs associated with the payment. | [optional] 
**schedule** | [**ExternalPaymentScheduleGet**](ExternalPaymentScheduleGet.md) |  | [optional] 
**scheme** | [**PaymentScheme**](PaymentScheme.md) |  | [optional] 
**status** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**transactionId** | **String** | The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts. | [optional] 
**walletId** | **String** | The EMI (E-Money Institution) wallet that this payment is associated with, if any. This wallet is used as an intermediary account to enable Plaid to reconcile the settlement of funds for Payment Initiation requests. | [optional] 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 


