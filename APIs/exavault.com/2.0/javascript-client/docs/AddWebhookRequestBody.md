# ExaVault.AddWebhookRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpointUrl** | **String** | The endpoint is where the webhook request will be sent. | 
**resource** | **String** | Resource identifier for the top folder this webhook is associated with | [optional] 
**responseVersion** | **String** | What version of webhook request should be sent to the endpoint URL when messages are sent | [optional] 
**triggers** | [**WebhookTriggers**](WebhookTriggers.md) |  | [optional] 



## Enum: ResponseVersionEnum


* `v1` (value: `"v1"`)

* `v2` (value: `"v2"`)




