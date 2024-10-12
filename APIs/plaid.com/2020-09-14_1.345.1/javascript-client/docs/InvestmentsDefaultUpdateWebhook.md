# ThePlaidApi.InvestmentsDefaultUpdateWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canceledInvestmentsTransactions** | **Number** | The number of canceled transactions reported since the last time this webhook was fired. | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**itemId** | **String** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**newInvestmentsTransactions** | **Number** | The number of new transactions reported since the last time this webhook was fired. | 
**webhookCode** | **String** | &#x60;DEFAULT_UPDATE&#x60; | 
**webhookType** | **String** | &#x60;INVESTMENTS_TRANSACTIONS&#x60; | 


