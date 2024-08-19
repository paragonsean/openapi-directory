# ThePlaidApi.PaymentInitiationRecipientCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | [optional] 
**bacs** | [**RecipientBACSNullable**](RecipientBACSNullable.md) |  | [optional] 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**iban** | **String** | The International Bank Account Number (IBAN) for the recipient. If BACS data is not provided, an IBAN is required. | [optional] 
**name** | **String** | The name of the recipient. We recommend using strings of length 18 or less and avoid special characters to ensure compatibility with all institutions. | 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 


