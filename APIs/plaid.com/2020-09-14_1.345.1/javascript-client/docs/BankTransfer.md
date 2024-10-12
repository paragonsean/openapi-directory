# ThePlaidApi.BankTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The account ID that should be credited/debited for this bank transfer. | 
**achClass** | [**ACHClass**](ACHClass.md) |  | 
**amount** | **String** | The amount of the bank transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**cancellable** | **Boolean** | When &#x60;true&#x60;, you can still cancel this bank transfer. | 
**created** | **Date** | The datetime when this bank transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | 
**customTag** | **String** | A string containing the custom tag provided by the client in the create request. Will be null if not provided. | 
**description** | **String** | The description of the transfer. | 
**direction** | [**BankTransferDirection**](BankTransferDirection.md) |  | 
**failureReason** | [**BankTransferFailure**](BankTransferFailure.md) |  | 
**id** | **String** | Plaid’s unique identifier for a bank transfer. | 
**isoCurrencyCode** | **String** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**metadata** | **{String: String}** | The Metadata object is a mapping of client-provided string fields to any string value. The following limitations apply: The JSON values must be Strings (no nested JSON objects allowed) Only ASCII characters may be used Maximum of 50 key/value pairs Maximum key length of 40 characters Maximum value length of 500 characters  | 
**network** | [**BankTransferNetwork**](BankTransferNetwork.md) |  | 
**originationAccountId** | **String** | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**status** | [**BankTransferStatus**](BankTransferStatus.md) |  | 
**type** | [**BankTransferType**](BankTransferType.md) |  | 
**user** | [**BankTransferUser**](BankTransferUser.md) |  | 


