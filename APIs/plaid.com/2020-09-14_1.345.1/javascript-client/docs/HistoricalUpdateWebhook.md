# ThePlaidApi.HistoricalUpdateWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**itemId** | **String** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**newTransactions** | **Number** | The number of new, unfetched transactions available | 
**webhookCode** | **String** | &#x60;HISTORICAL_UPDATE&#x60; | 
**webhookType** | **String** | &#x60;TRANSACTIONS&#x60; | 


