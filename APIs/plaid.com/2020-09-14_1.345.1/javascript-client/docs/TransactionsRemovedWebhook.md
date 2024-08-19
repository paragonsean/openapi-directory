# ThePlaidApi.TransactionsRemovedWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**itemId** | **String** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**removedTransactions** | **[String]** | An array of &#x60;transaction_ids&#x60; corresponding to the removed transactions | 
**webhookCode** | **String** | &#x60;TRANSACTIONS_REMOVED&#x60; | 
**webhookType** | **String** | &#x60;TRANSACTIONS&#x60; | 


