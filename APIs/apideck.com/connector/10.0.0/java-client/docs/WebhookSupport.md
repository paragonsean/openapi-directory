

# WebhookSupport

How webhooks are supported for the connector. Sometimes the connector natively supports webhooks, other times Apideck virtualizes them based on polling.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**managedVia** | [**ManagedViaEnum**](#ManagedViaEnum) | How the subscription is managed in the downstream. |  [optional] |
|**mode** | [**ModeEnum**](#ModeEnum) | Mode of the webhook support. |  [optional] |
|**subscriptionLevel** | [**SubscriptionLevelEnum**](#SubscriptionLevelEnum) | Received events are scoped to connection or across integration. |  [optional] |
|**virtualWebhooks** | [**VirtualWebhooks**](VirtualWebhooks.md) |  |  [optional] |



## Enum: ManagedViaEnum

| Name | Value |
|---- | -----|
| MANUAL | &quot;manual&quot; |
| API | &quot;api&quot; |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| NATIVE | &quot;native&quot; |
| VIRTUAL | &quot;virtual&quot; |
| NONE | &quot;none&quot; |



## Enum: SubscriptionLevelEnum

| Name | Value |
|---- | -----|
| CONNECTION | &quot;connection&quot; |
| INTEGRATION | &quot;integration&quot; |



