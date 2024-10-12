

# Webhook


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdAt** | **OffsetDateTime** | The date and time when the object was created. |  [optional] [readonly] |
|**deliveryUrl** | **URI** | The delivery url of the webhook endpoint. |  |
|**description** | **String** | A description of the object. |  [optional] |
|**disabledReason** | [**DisabledReasonEnum**](#DisabledReasonEnum) | Indicates if the webhook has has been disabled as it reached its retry limit or if account is over the usage allocated by it&#39;s plan. |  [optional] |
|**events** | **List&lt;WebhookEventType&gt;** | The list of subscribed events for this webhook. [&#x60;*&#x60;] indicates that all events are enabled. |  |
|**executeBaseUrl** | **URI** | The Unify Base URL events from connectors will be sent to after service id is appended. |  [readonly] |
|**id** | **String** |  |  [optional] [readonly] |
|**status** | **Status** |  |  |
|**unifiedApi** | **UnifiedApiId** |  |  |
|**updatedAt** | **OffsetDateTime** | The date and time when the object was last updated. |  [optional] [readonly] |



## Enum: DisabledReasonEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| RETRY_LIMIT | &quot;retry_limit&quot; |
| USAGE_LIMIT | &quot;usage_limit&quot; |



