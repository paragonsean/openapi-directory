

# NotificationAttributes

Attributes for the notification including the path, recipients, and share data. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**action** | [**ActionEnum**](#ActionEnum) | Action that triggers notification. |  [optional] |
|**created** | **OffsetDateTime** | Timestamp of notifiction creation. |  [optional] |
|**message** | **String** | Custom message that will be sent to the notification recipients. |  [optional] |
|**modified** | **OffsetDateTime** | Timestamp of notification modification. |  [optional] |
|**name** | **String** | Name of the item that the notification is set on. |  [optional] |
|**path** | **String** | Path to the item that the notification is set on. |  [optional] |
|**readableDescription** | **String** | Human readable description of the notification. |  [optional] |
|**readableDescriptionWithoutPath** | **String** | Human readable description of the notification without item path. |  [optional] |
|**recipients** | [**List&lt;NotificationRecipient&gt;**](NotificationRecipient.md) | Notification recipients. |  [optional] |
|**sendEmail** | **Boolean** | Whether or not an email will send when the notification is triggered. |  [optional] |
|**shareId** | **String** | ID of the share that the notification belogns to. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the resource the notification is attached to.  |  [optional] |
|**userId** | **String** | ID of the user that the notification belongs to. |  [optional] |
|**usernames** | **List&lt;String&gt;** | Detail on which users can trigger the notification. |  [optional] |



## Enum: ActionEnum

| Name | Value |
|---- | -----|
| UPLOAD | &quot;upload&quot; |
| DOWNLOAD | &quot;download&quot; |
| DELETE | &quot;delete&quot; |
| ALL | &quot;all&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FILE | &quot;file&quot; |
| FOLDER | &quot;folder&quot; |
| SHARED_FOLDER | &quot;shared_folder&quot; |
| SEND_RECEIPT | &quot;send_receipt&quot; |
| SHARE_RECEIPT | &quot;share_receipt&quot; |
| FILE_DROP | &quot;file_drop&quot; |



