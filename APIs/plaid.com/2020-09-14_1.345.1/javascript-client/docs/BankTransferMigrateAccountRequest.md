# ThePlaidApi.BankTransferMigrateAccountRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountNumber** | **String** | The user&#39;s account number. | 
**accountType** | **String** | The type of the bank account (&#x60;checking&#x60; or &#x60;savings&#x60;). | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**routingNumber** | **String** | The user&#39;s routing number. | 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**wireRoutingNumber** | **String** | The user&#39;s wire transfer routing number. This is the ABA number; for some institutions, this may differ from the ACH number used in &#x60;routing_number&#x60;. | [optional] 


