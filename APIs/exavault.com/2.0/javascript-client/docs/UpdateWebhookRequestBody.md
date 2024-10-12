# ExaVault.UpdateWebhookRequestBody

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpointUrl** | **String** | New endpoint URL to use for the webhook configuration | [optional] 
**resource** | **String** | Resource identifier of the top folder watched by this webhook. | [optional] 
**responseVersion** | **String** | Version of the webhooks message to send to the endpoint | [optional] 
**triggers** | [**WebhookTriggers**](WebhookTriggers.md) |  | [optional] 



## Enum: ResponseVersionEnum


* `v2` (value: `"v2"`)

* `v1` (value: `"v1"`)




