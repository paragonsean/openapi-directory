# ExaVault.NotificationAttributes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **String** | Action that triggers notification. | [optional] 
**created** | **Date** | Timestamp of notifiction creation. | [optional] 
**message** | **String** | Custom message that will be sent to the notification recipients. | [optional] 
**modified** | **Date** | Timestamp of notification modification. | [optional] 
**name** | **String** | Name of the item that the notification is set on. | [optional] 
**path** | **String** | Path to the item that the notification is set on. | [optional] 
**readableDescription** | **String** | Human readable description of the notification. | [optional] 
**readableDescriptionWithoutPath** | **String** | Human readable description of the notification without item path. | [optional] 
**recipients** | [**[NotificationRecipient]**](NotificationRecipient.md) | Notification recipients. | [optional] 
**sendEmail** | **Boolean** | Whether or not an email will send when the notification is triggered. | [optional] 
**shareId** | **String** | ID of the share that the notification belogns to. | [optional] 
**type** | **String** | Type of the resource the notification is attached to.  | [optional] 
**userId** | **String** | ID of the user that the notification belongs to. | [optional] 
**usernames** | **[String]** | Detail on which users can trigger the notification. | [optional] 



## Enum: ActionEnum


* `upload` (value: `"upload"`)

* `download` (value: `"download"`)

* `delete` (value: `"delete"`)

* `all` (value: `"all"`)





## Enum: TypeEnum


* `file` (value: `"file"`)

* `folder` (value: `"folder"`)

* `shared_folder` (value: `"shared_folder"`)

* `send_receipt` (value: `"send_receipt"`)

* `share_receipt` (value: `"share_receipt"`)

* `file_drop` (value: `"file_drop"`)




