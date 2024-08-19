# ThePlaidApi.HoldingsDefaultUpdateWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | [optional] 
**itemId** | **String** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**newHoldings** | **Number** | The number of new holdings reported since the last time this webhook was fired. | 
**updatedHoldings** | **Number** | The number of updated holdings reported since the last time this webhook was fired. | 
**webhookCode** | **String** | &#x60;DEFAULT_UPDATE&#x60; | 
**webhookType** | **String** | &#x60;HOLDINGS&#x60; | 


