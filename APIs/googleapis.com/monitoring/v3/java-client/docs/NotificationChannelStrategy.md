

# NotificationChannelStrategy

Control over how the notification channels in notification_channels are notified when this alert fires, on a per-channel basis.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**notificationChannelNames** | **List&lt;String&gt;** | The full REST resource name for the notification channels that these settings apply to. Each of these correspond to the name field in one of the NotificationChannel objects referenced in the notification_channels field of this AlertPolicy. The format is: projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]  |  [optional] |
|**renotifyInterval** | **String** | The frequency at which to send reminder notifications for open incidents. |  [optional] |



