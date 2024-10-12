

# NotificationSet

A resource returned by the PullNotificationSet API, which contains a collection of notifications for enterprises associated with the service account authenticated for the request.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**notification** | [**List&lt;Notification&gt;**](Notification.md) | The notifications received, or empty if no notifications are present. |  [optional] |
|**notificationSetId** | **String** | The notification set ID, required to mark the notification as received with the Enterprises.AcknowledgeNotification API. This will be omitted if no notifications are present. |  [optional] |



