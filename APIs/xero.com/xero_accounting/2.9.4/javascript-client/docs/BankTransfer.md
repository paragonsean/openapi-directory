# XeroAccountingApi.BankTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | amount of the transaction | 
**bankTransferID** | **String** | The identifier of the Bank Transfer | [optional] [readonly] 
**createdDateUTC** | **String** | UTC timestamp of creation date of bank transfer | [optional] [readonly] 
**currencyRate** | **Number** | The currency rate | [optional] [readonly] 
**date** | **String** | The date of the Transfer YYYY-MM-DD | [optional] 
**fromBankAccount** | [**Account**](Account.md) |  | 
**fromBankTransactionID** | **String** | The Bank Transaction ID for the source account | [optional] [readonly] 
**hasAttachments** | **Boolean** | Boolean to indicate if a Bank Transfer has an attachment | [optional] [readonly] [default to false]
**toBankAccount** | [**Account**](Account.md) |  | 
**toBankTransactionID** | **String** | The Bank Transaction ID for the destination account | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 


