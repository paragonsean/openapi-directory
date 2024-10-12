# ThePlaidApi.IdentityDefaultUpdateWebhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountIdsWithUpdatedIdentity** | **{String: [IdentityUpdateTypes]}** | An object with keys of &#x60;account_id&#x60;&#39;s that are mapped to their respective identity attributes that changed.  Example: &#x60;{ \&quot;XMBvvyMGQ1UoLbKByoMqH3nXMj84ALSdE5B58\&quot;: [\&quot;PHONES\&quot;] }&#x60;  | 
**environment** | [**WebhookEnvironmentValues**](WebhookEnvironmentValues.md) |  | 
**error** | [**PlaidError**](PlaidError.md) |  | 
**itemId** | **String** | The &#x60;item_id&#x60; of the Item associated with this webhook, warning, or error | 
**webhookCode** | **String** | &#x60;DEFAULT_UPDATE&#x60; | 
**webhookType** | **String** | &#x60;IDENTITY&#x60; | 


