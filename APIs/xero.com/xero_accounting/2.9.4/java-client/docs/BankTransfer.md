

# BankTransfer


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amount** | **Double** | amount of the transaction |  |
|**bankTransferID** | **UUID** | The identifier of the Bank Transfer |  [optional] [readonly] |
|**createdDateUTC** | **String** | UTC timestamp of creation date of bank transfer |  [optional] [readonly] |
|**currencyRate** | **Double** | The currency rate |  [optional] [readonly] |
|**date** | **String** | The date of the Transfer YYYY-MM-DD |  [optional] |
|**fromBankAccount** | [**Account**](Account.md) |  |  |
|**fromBankTransactionID** | **UUID** | The Bank Transaction ID for the source account |  [optional] [readonly] |
|**hasAttachments** | **Boolean** | Boolean to indicate if a Bank Transfer has an attachment |  [optional] [readonly] |
|**toBankAccount** | [**Account**](Account.md) |  |  |
|**toBankTransactionID** | **UUID** | The Bank Transaction ID for the destination account |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



