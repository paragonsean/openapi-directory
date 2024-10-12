# ThePlaidApi.PaymentInitiationPaymentCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**PaymentAmount**](PaymentAmount.md) |  | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**options** | [**ExternalPaymentOptions**](ExternalPaymentOptions.md) |  | [optional] 
**recipientId** | **String** | The ID of the recipient the payment is for. | 
**reference** | **String** | A reference for the payment. This must be an alphanumeric string with at most 18 characters and must not contain any special characters (since not all institutions support them). In order to track settlement via Payment Confirmation, each payment must have a unique reference. If the reference provided through the API is not unique, Plaid will adjust it. Both the originally provided and automatically adjusted references (if any) can be found in the &#x60;reference&#x60; and &#x60;adjusted_reference&#x60; fields, respectively. | 
**schedule** | [**ExternalPaymentScheduleRequest**](ExternalPaymentScheduleRequest.md) |  | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 


