

# NotificationChannelProperties

Properties of a schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createdDate** | **OffsetDateTime** | The creation date of the notification channel. |  [optional] [readonly] |
|**description** | **String** | Description of notification. |  [optional] |
|**events** | [**List&lt;Event&gt;**](Event.md) | The list of event for which this notification is enabled. |  [optional] |
|**provisioningState** | **String** | The provisioning status of the resource. |  [optional] |
|**uniqueIdentifier** | **String** | The unique immutable identifier of a resource (Guid). |  [optional] |
|**webHookUrl** | **String** | The webhook URL to send notifications to. |  [optional] |



