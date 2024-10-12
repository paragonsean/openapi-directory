

# AlertNotificationProperties

The properties of the alert notification settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalRecipientEmailList** | **List&lt;String&gt;** | The alert notification email list. |  [optional] |
|**alertNotificationCulture** | **String** | The alert notification culture. |  [optional] |
|**emailNotification** | [**EmailNotificationEnum**](#EmailNotificationEnum) | Indicates whether email notification enabled or not. |  |
|**notificationToServiceOwners** | [**NotificationToServiceOwnersEnum**](#NotificationToServiceOwnersEnum) | The value indicating whether alert notification enabled for admin or not. |  [optional] |



## Enum: EmailNotificationEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: NotificationToServiceOwnersEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



