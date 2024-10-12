# ThePlaidApi.TransactionsRecurringGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inflowStreams** | [**[TransactionStream]**](TransactionStream.md) | An array of depository transaction streams. | 
**outflowStreams** | [**[TransactionStream]**](TransactionStream.md) | An array of expense transaction streams. | 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**updatedDatetime** | **Date** | Timestamp in [ISO 8601](https://wikipedia.org/wiki/ISO_8601) format (&#x60;YYYY-MM-DDTHH:mm:ssZ&#x60;) indicating the last time transaction streams for the given account were updated on | 


