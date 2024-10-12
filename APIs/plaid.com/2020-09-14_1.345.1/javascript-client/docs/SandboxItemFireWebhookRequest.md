# ThePlaidApi.SandboxItemFireWebhookRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The access token associated with the Item data is being requested for. | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 
**webhookCode** | **String** | The webhook codes that can be fired by this test endpoint. | 
**webhookType** | [**WebhookType**](WebhookType.md) |  | [optional] 



## Enum: WebhookCodeEnum


* `DEFAULT_UPDATE` (value: `"DEFAULT_UPDATE"`)

* `NEW_ACCOUNTS_AVAILABLE` (value: `"NEW_ACCOUNTS_AVAILABLE"`)

* `AUTH_DATA_UPDATE` (value: `"AUTH_DATA_UPDATE"`)

* `RECURRING_TRANSACTIONS_UPDATE` (value: `"RECURRING_TRANSACTIONS_UPDATE"`)

* `SYNC_UPDATES_AVAILABLE` (value: `"SYNC_UPDATES_AVAILABLE"`)




