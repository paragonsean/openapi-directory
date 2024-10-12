# ThePlaidApi.LiabilitiesDefaultUpdateWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountIdsWithNewLiabilities** | **[String]** | An array of &#x60;account_id&#x60;&#39;s for accounts that contain new liabilities.&#39; | 
**accountIdsWithUpdatedLiabilities** | **{String: [String]}** | An object with keys of &#x60;account_id&#x60;&#39;s that are mapped to their respective liabilities fields that changed.  Example: &#x60;{ \&quot;XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58\&quot;: [\&quot;past_amount_due\&quot;] }&#x60;  | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | 
**itemId** | **String** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**webhookCode** | **String** | &#x60;DEFAULT_UPDATE&#x60; | 
**webhookType** | **String** | &#x60;LIABILITIES&#x60; | 


