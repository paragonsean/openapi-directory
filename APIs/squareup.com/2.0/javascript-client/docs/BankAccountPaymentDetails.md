# SquareConnectApi.BankAccountPaymentDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountOwnershipType** | **String** | The ownership type of the bank account performing the transfer. The type can be &#x60;INDIVIDUAL&#x60;, &#x60;COMPANY&#x60;, or &#x60;UNKNOWN&#x60;. | [optional] 
**achDetails** | [**ACHDetails**](ACHDetails.md) |  | [optional] 
**bankName** | **String** | The name of the bank associated with the bank account. | [optional] 
**country** | **String** | The two-letter ISO code representing the country the bank account is located in. | [optional] 
**errors** | [**[Error]**](Error.md) | Information about errors encountered during the request. | [optional] 
**fingerprint** | **String** | Uniquely identifies the bank account for this seller and can be used to determine if payments are from the same bank account. | [optional] 
**statementDescription** | **String** | The statement description as sent to the bank. | [optional] 
**transferType** | **String** | The type of the bank transfer. The type can be &#x60;ACH&#x60; or &#x60;UNKNOWN&#x60;. | [optional] 


