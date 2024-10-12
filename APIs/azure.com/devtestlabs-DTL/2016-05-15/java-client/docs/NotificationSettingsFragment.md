

# NotificationSettingsFragment

Notification settings for a schedule.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**status** | [**StatusEnum**](#StatusEnum) | If notifications are enabled for this schedule (i.e. Enabled, Disabled). |  [optional] |
|**timeInMinutes** | **Integer** | Time in minutes before event at which notification will be sent. |  [optional] |
|**webhookUrl** | **String** | The webhook URL to which the notification will be sent. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



