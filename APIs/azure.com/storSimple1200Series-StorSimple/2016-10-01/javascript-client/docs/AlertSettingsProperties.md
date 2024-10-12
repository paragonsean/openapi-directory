# StorSimpleManagementClient.AlertSettingsProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalRecipientEmailList** | **[String]** | List of email addresses (apart from admin/co-admin of subscription) to whom the alert emails need to be sent | [optional] 
**alertNotificationCulture** | **String** | Culture setting to be used while building alert emails. For eg: \&quot;en-US\&quot; | 
**emailNotification** | **String** | Value indicating whether user/admins will receive emails when an alert condition occurs on the system | 
**notificationToServiceOwners** | **String** | Value indicating whether service owners will receive emails when an alert condition occurs on the system. Applicable only if emailNotification flag is Enabled. | 



## Enum: EmailNotificationEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)





## Enum: NotificationToServiceOwnersEnum


* `Enabled` (value: `"Enabled"`)

* `Disabled` (value: `"Disabled"`)




