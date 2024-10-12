# WebhookApi.Webhook

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The date and time when the object was created. | [optional] [readonly] 
**deliveryUrl** | **String** | The delivery url of the webhook endpoint. | 
**description** | **String** | A description of the object. | [optional] 
**disabledReason** | **String** | Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it&#39;s plan. | [optional] 
**events** | [**[WebhookEventType]**](WebhookEventType.md) | The list of subscribed events for this webhook. [&#x60;*&#x60;] indicates that all events are enabled. | 
**executeBaseUrl** | **String** | The Unify Base URL events from connectors will be sent to after service id is appended. | [readonly] 
**id** | **String** |  | [optional] [readonly] 
**status** | [**Status**](Status.md) |  | 
**unifiedApi** | [**UnifiedApiId**](UnifiedApiId.md) |  | 
**updatedAt** | **Date** | The date and time when the object was last updated. | [optional] [readonly] 



## Enum: DisabledReasonEnum


* `none` (value: `"none"`)

* `retry_limit` (value: `"retry_limit"`)

* `usage_limit` (value: `"usage_limit"`)




