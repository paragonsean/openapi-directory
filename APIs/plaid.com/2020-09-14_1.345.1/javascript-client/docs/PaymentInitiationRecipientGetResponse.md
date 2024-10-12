# ThePlaidApi.PaymentInitiationRecipientGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**PaymentInitiationAddress**](PaymentInitiationAddress.md) |  | [optional] 
**bacs** | [**RecipientBACSNullable**](RecipientBACSNullable.md) |  | [optional] 
**iban** | **String** | The International Bank Account Number (IBAN) for the recipient. | [optional] 
**name** | **String** | The name of the recipient. | 
**recipientId** | **String** | The ID of the recipient. | 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 


