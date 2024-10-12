# ThePlaidApi.PaymentStatusUpdateWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustedReference** | **String** | The value of the reference sent to the bank after adjustment to pass bank validation rules. | [optional] 
**adjustedStartDate** | **Date** | The start date sent to the bank after adjusting for holidays or weekends.  Will be provided in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD). If the start date did not require adjustment, or if the payment is not a standing order, this field will be &#x60;null&#x60;. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**newPaymentStatus** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**oldPaymentStatus** | [**PaymentInitiationPaymentStatus**](PaymentInitiationPaymentStatus.md) |  | 
**originalReference** | **String** | The original value of the reference when creating the payment. | 
**originalStartDate** | **Date** | The original value of the &#x60;start_date&#x60; provided during the creation of a standing order. If the payment is not a standing order, this field will be &#x60;null&#x60;. | 
**paymentId** | **String** | The &#x60;payment_id&#x60; for the payment being updated | 
**timestamp** | **Date** | The timestamp of the update, in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format, e.g. &#x60;\&quot;2017-09-14T14:42:19.350Z\&quot;&#x60; | 
**transactionId** | **String** | The transaction ID that this payment is associated with, if any. This is present only when a payment was initiated using virtual accounts. | [optional] 
**webhookCode** | **String** | &#x60;PAYMENT_STATUS_UPDATE&#x60; | 
**webhookType** | **String** | &#x60;PAYMENT_INITIATION&#x60; | 


