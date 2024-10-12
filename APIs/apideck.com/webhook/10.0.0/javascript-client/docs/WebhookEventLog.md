# WebhookApi.WebhookEventLog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationId** | **String** | ID of your Apideck Application | [optional] 
**attempts** | [**[WebhookEventLogAttemptsInner]**](WebhookEventLogAttemptsInner.md) | record of each attempt to call webhook endpoint | [optional] 
**consumerId** | **String** | Unique consumer identifier. You can freely choose a consumer ID yourself. Most of the time, this is an ID of your internal data model that represents a user or account in your system (for example account:12345). If the consumer doesn&#39;t exist yet, Vault will upsert a consumer based on your ID. | [optional] 
**endpoint** | **String** | The URL of the webhook endpoint. | [optional] 
**entityType** | **String** | Name of the Entity described by the attributes delivered within payload | [optional] 
**eventType** | **String** | Name of source event that webhook is subscribed to. | [optional] 
**executionAttempt** | **Number** | Number of attempts webhook endpoint was called before a success was returned or eventually failed | [optional] 
**httpMethod** | **String** | HTTP Method of request to endpoint. | [optional] 
**id** | **String** |  | [optional] 
**requestBody** | **String** | The JSON stringified payload that was delivered to the webhook endpoint. | [optional] 
**responseBody** | **String** | The JSON stringified response that was returned from the webhook endpoint. | [optional] 
**retryScheduled** | **Boolean** | If the request has not hit the max retry limit and will be retried. | [optional] 
**service** | [**WebhookEventLogService**](WebhookEventLogService.md) |  | [optional] 
**statusCode** | **Number** | HTTP Status code that was returned. | [optional] 
**success** | **Boolean** | Whether or not the request was successful. | [optional] 
**timestamp** | **String** | ISO Date and time when the request was made. | [optional] 
**unifiedApi** | [**UnifiedApiId**](UnifiedApiId.md) |  | [optional] 


