

# NotificationEntity

List Notifications

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**groupId** | **Integer** | Notification group id |  [optional] |
|**groupName** | **String** | Group name if applicable |  [optional] |
|**id** | **Integer** | Notification ID |  [optional] |
|**message** | **String** | Custom message to include in notification emails. |  [optional] |
|**notifyOnCopy** | **Boolean** | Triggers notification when copying files to this path |  [optional] |
|**notifyOnDelete** | **Boolean** | Triggers notification when deleting files from this path |  [optional] |
|**notifyOnDownload** | **Boolean** | Triggers notification when downloading files from this path |  [optional] |
|**notifyOnMove** | **Boolean** | Triggers notification when moving files to this path |  [optional] |
|**notifyOnUpload** | **Boolean** | Triggers notification when uploading new files to this path |  [optional] |
|**notifyUserActions** | **Boolean** | Trigger notification on notification user actions? |  [optional] |
|**path** | **String** | Folder path to notify on |  [optional] |
|**recursive** | **Boolean** | Enable notifications for each subfolder in this path |  [optional] |
|**sendInterval** | [**SendIntervalEnum**](#SendIntervalEnum) | The time interval that notifications are aggregated to |  [optional] |
|**suppressedEmail** | **Boolean** | If true, it means that the recipient at this user&#39;s email address has manually unsubscribed from all emails, or had their email \&quot;hard bounce\&quot;, which means that we are unable to send mail to this user&#39;s current email address. Notifications will resume if the user changes their email address. |  [optional] |
|**triggerByShareRecipients** | **Boolean** | Notify when actions are performed by a share recipient? |  [optional] |
|**triggeringFilenames** | **List&lt;String&gt;** | Array of filenames (possibly with wildcards) to match for action path |  [optional] |
|**triggeringGroupIds** | **List&lt;Integer&gt;** | Only notify on actions made by a member of one of the specified groups |  [optional] |
|**triggeringUserIds** | **List&lt;Integer&gt;** | Only notify on actions made one of the specified users |  [optional] |
|**unsubscribed** | **Boolean** | Is the user unsubscribed from this notification? |  [optional] |
|**unsubscribedReason** | [**UnsubscribedReasonEnum**](#UnsubscribedReasonEnum) | The reason that the user unsubscribed |  [optional] |
|**userId** | **Integer** | Notification user ID |  [optional] |
|**username** | **String** | Notification username |  [optional] |



## Enum: SendIntervalEnum

| Name | Value |
|---- | -----|
| FIVE_MINUTES | &quot;five_minutes&quot; |
| FIFTEEN_MINUTES | &quot;fifteen_minutes&quot; |
| HOURLY | &quot;hourly&quot; |
| DAILY | &quot;daily&quot; |



## Enum: UnsubscribedReasonEnum

| Name | Value |
|---- | -----|
| NONE | &quot;none&quot; |
| UNSUBSCRIBE_LINK_CLICKED | &quot;unsubscribe_link_clicked&quot; |
| MAIL_BOUNCED | &quot;mail_bounced&quot; |
| MAIL_MARKED_AS_SPAM | &quot;mail_marked_as_spam&quot; |



