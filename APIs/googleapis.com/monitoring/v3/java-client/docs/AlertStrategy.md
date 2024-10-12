

# AlertStrategy

Control over how the notification channels in notification_channels are notified when this alert fires.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoClose** | **String** | If an alert policy that was active has no data for this long, any open incidents will close |  [optional] |
|**notificationChannelStrategy** | [**List&lt;NotificationChannelStrategy&gt;**](NotificationChannelStrategy.md) | Control how notifications will be sent out, on a per-channel basis. |  [optional] |
|**notificationRateLimit** | [**NotificationRateLimit**](NotificationRateLimit.md) |  |  [optional] |



