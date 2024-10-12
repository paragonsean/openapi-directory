# FilesComApi.NotificationEntity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groupId** | **Number** | Notification group id | [optional] 
**groupName** | **String** | Group name if applicable | [optional] 
**id** | **Number** | Notification ID | [optional] 
**message** | **String** | Custom message to include in notification emails. | [optional] 
**notifyOnCopy** | **Boolean** | Triggers notification when copying files to this path | [optional] 
**notifyOnDelete** | **Boolean** | Triggers notification when deleting files from this path | [optional] 
**notifyOnDownload** | **Boolean** | Triggers notification when downloading files from this path | [optional] 
**notifyOnMove** | **Boolean** | Triggers notification when moving files to this path | [optional] 
**notifyOnUpload** | **Boolean** | Triggers notification when uploading new files to this path | [optional] 
**notifyUserActions** | **Boolean** | Trigger notification on notification user actions? | [optional] 
**path** | **String** | Folder path to notify on | [optional] 
**recursive** | **Boolean** | Enable notifications for each subfolder in this path | [optional] 
**sendInterval** | **String** | The time interval that notifications are aggregated to | [optional] 
**suppressedEmail** | **Boolean** | If true, it means that the recipient at this user&#39;s email address has manually unsubscribed from all emails, or had their email \&quot;hard bounce\&quot;, which means that we are unable to send mail to this user&#39;s current email address. Notifications will resume if the user changes their email address. | [optional] 
**triggerByShareRecipients** | **Boolean** | Notify when actions are performed by a share recipient? | [optional] 
**triggeringFilenames** | **[String]** | Array of filenames (possibly with wildcards) to match for action path | [optional] 
**triggeringGroupIds** | **[Number]** | Only notify on actions made by a member of one of the specified groups | [optional] 
**triggeringUserIds** | **[Number]** | Only notify on actions made one of the specified users | [optional] 
**unsubscribed** | **Boolean** | Is the user unsubscribed from this notification? | [optional] 
**unsubscribedReason** | **String** | The reason that the user unsubscribed | [optional] 
**userId** | **Number** | Notification user ID | [optional] 
**username** | **String** | Notification username | [optional] 



## Enum: SendIntervalEnum


* `five_minutes` (value: `"five_minutes"`)

* `fifteen_minutes` (value: `"fifteen_minutes"`)

* `hourly` (value: `"hourly"`)

* `daily` (value: `"daily"`)





## Enum: UnsubscribedReasonEnum


* `none` (value: `"none"`)

* `unsubscribe_link_clicked` (value: `"unsubscribe_link_clicked"`)

* `mail_bounced` (value: `"mail_bounced"`)

* `mail_marked_as_spam` (value: `"mail_marked_as_spam"`)




