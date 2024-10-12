# VaultApi.ConnectionEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**ConsumerConnection**](ConsumerConnection.md) |  | [optional] 
**entityId** | **String** | The service provider&#39;s ID of the entity that triggered this event | [optional] 
**entityType** | **String** | The type entity that triggered this event | [optional] 
**eventId** | **String** | Unique reference to this request event | [optional] 
**eventType** | [**VaultEventType**](VaultEventType.md) |  | [optional] 
**executionAttempt** | **Number** | The current count this request event has been attempted | [optional] 
**occurredAt** | **String** | ISO Datetime for when the original event occurred | [optional] 
**serviceId** | **String** | Service provider identifier | [optional] 


