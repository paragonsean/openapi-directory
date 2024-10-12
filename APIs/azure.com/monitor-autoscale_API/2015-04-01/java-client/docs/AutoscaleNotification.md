

# AutoscaleNotification

Autoscale notification.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**email** | [**EmailNotification**](EmailNotification.md) |  |  [optional] |
|**operation** | [**OperationEnum**](#OperationEnum) | the operation associated with the notification and its value must be \&quot;scale\&quot; |  |
|**webhooks** | [**List&lt;WebhookNotification&gt;**](WebhookNotification.md) | the collection of webhook notifications. |  [optional] |



## Enum: OperationEnum

| Name | Value |
|---- | -----|
| SCALE | &quot;Scale&quot; |



