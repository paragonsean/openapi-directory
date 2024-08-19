

# AlertSettingsProperties

Class containing the properties of AlertSettings

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalRecipientEmailList** | **List&lt;String&gt;** | List of email addresses (apart from admin/co-admin of subscription) to whom the alert emails need to be sent |  [optional] |
|**alertNotificationCulture** | **String** | Culture setting to be used while building alert emails. For eg: \&quot;en-US\&quot; |  |
|**emailNotification** | [**EmailNotificationEnum**](#EmailNotificationEnum) | Value indicating whether user/admins will receive emails when an alert condition occurs on the system |  |
|**notificationToServiceOwners** | [**NotificationToServiceOwnersEnum**](#NotificationToServiceOwnersEnum) | Value indicating whether service owners will receive emails when an alert condition occurs on the system. Applicable only if emailNotification flag is Enabled. |  |



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



