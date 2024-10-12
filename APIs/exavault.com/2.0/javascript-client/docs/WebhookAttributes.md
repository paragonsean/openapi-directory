# ExaVault.WebhookAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Date** | Timestamp when webhook configuration was added to system. | [optional] 
**endpointUrl** | **String** | The endpoint is where the webhook request will be sent. | [optional] 
**failed** | **Boolean** | Whether webhook has been disabled for too many consecutive failures | [optional] 
**modified** | **Date** | Timestamp when webhook configuration was last modified | [optional] 
**responseVersion** | **String** | The version of webhook request to send to the endpoint URL | [optional] 
**triggers** | [**WebhookTriggers**](WebhookTriggers.md) |  | [optional] 
**verificationToken** | **String** | Token for verifying sender is ExaVault | [optional] 



## Enum: ResponseVersionEnum


* `v1` (value: `"v1"`)

* `v2` (value: `"v2"`)




