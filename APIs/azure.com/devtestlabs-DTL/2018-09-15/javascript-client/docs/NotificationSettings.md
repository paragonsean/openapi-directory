# DevTestLabsClient.NotificationSettings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emailRecipient** | **String** | The email recipient to send notifications to (can be a list of semi-colon separated email addresses). | [optional] 
**notificationLocale** | **String** | The locale to use when sending a notification (fallback for unsupported languages is EN). | [optional] 
**status** | **String** | If notifications are enabled for this schedule (i.e. Enabled, Disabled). | [optional] 
**timeInMinutes** | **Number** | Time in minutes before event at which notification will be sent. | [optional] 
**webhookUrl** | **String** | The webhook URL to which the notification will be sent. | [optional] 



## Enum: StatusEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




