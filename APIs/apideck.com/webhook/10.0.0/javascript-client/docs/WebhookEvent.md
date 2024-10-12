# WebhookApi.WebhookEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityId** | **String** | The service provider&#39;s ID of the entity that triggered this event | [optional] 
**entityType** | **String** | The type entity that triggered this event | [optional] 
**entityUrl** | **String** | The url to retrieve entity detail. | [optional] 
**eventId** | **String** | Unique reference to this request event | [optional] 
**eventType** | [**WebhookEventType**](WebhookEventType.md) |  | [optional] 
**executionAttempt** | **Number** | The current count this request event has been attempted | [optional] 
**occurredAt** | **Date** | ISO Datetime for when the original event occurred | [optional] 
**serviceId** | **String** | Service provider identifier | [optional] 


