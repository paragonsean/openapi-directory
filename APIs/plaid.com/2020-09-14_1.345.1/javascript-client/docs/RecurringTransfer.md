# ThePlaidApi.RecurringTransfer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The Plaid &#x60;account_id&#x60; corresponding to the end-user account that will be debited or credited. | 
**achClass** | [**ACHClass**](ACHClass.md) |  | [optional] 
**amount** | **String** | The amount of the transfer (decimal string with two digits of precision e.g. \&quot;10.00\&quot;). | 
**created** | **Date** | The datetime when this transfer was created. This will be of the form &#x60;2006-01-02T15:04:05Z&#x60; | 
**description** | **String** | The description of the recurring transfer. | 
**fundingAccountId** | **String** | The id of the funding account to use, available in the Plaid Dashboard. This determines which of your business checking accounts will be credited or debited. | 
**isoCurrencyCode** | **String** | The currency of the transfer amount, e.g. \&quot;USD\&quot; | 
**network** | [**TransferNetwork**](TransferNetwork.md) |  | 
**nextOriginationDate** | **Date** | A date in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (YYYY-MM-DD).  The next transfer origination date after bank holiday adjustment. | 
**originationAccountId** | **String** | Plaid’s unique identifier for the origination account that was used for this transfer. | 
**recurringTransferId** | **String** | Plaid’s unique identifier for a recurring transfer. | 
**schedule** | [**TransferRecurringSchedule**](TransferRecurringSchedule.md) |  | 
**status** | [**TransferRecurringStatus**](TransferRecurringStatus.md) |  | 
**testClockId** | **String** | Plaid’s unique identifier for a test clock. | [optional] 
**transferIds** | **[String]** |  | 
**type** | [**TransferType**](TransferType.md) |  | 
**user** | [**TransferUserInResponse**](TransferUserInResponse.md) |  | 


