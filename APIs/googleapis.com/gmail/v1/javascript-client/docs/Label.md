# GmailApi.Label

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**color** | [**LabelColor**](LabelColor.md) |  | [optional] 
**id** | **String** | The immutable ID of the label. | [optional] 
**labelListVisibility** | **String** | The visibility of the label in the label list in the Gmail web interface. | [optional] 
**messageListVisibility** | **String** | The visibility of messages with this label in the message list in the Gmail web interface. | [optional] 
**messagesTotal** | **Number** | The total number of messages with the label. | [optional] 
**messagesUnread** | **Number** | The number of unread messages with the label. | [optional] 
**name** | **String** | The display name of the label. | [optional] 
**threadsTotal** | **Number** | The total number of threads with the label. | [optional] 
**threadsUnread** | **Number** | The number of unread threads with the label. | [optional] 
**type** | **String** | The owner type for the label. User labels are created by the user and can be modified and deleted by the user and can be applied to any message or thread. System labels are internally created and cannot be added, modified, or deleted. System labels may be able to be applied to or removed from messages and threads under some circumstances but this is not guaranteed. For example, users can apply and remove the &#x60;INBOX&#x60; and &#x60;UNREAD&#x60; labels from messages and threads, but cannot apply or remove the &#x60;DRAFTS&#x60; or &#x60;SENT&#x60; labels from messages or threads. | [optional] 



## Enum: LabelListVisibilityEnum


* `labelShow` (value: `"labelShow"`)

* `labelShowIfUnread` (value: `"labelShowIfUnread"`)

* `labelHide` (value: `"labelHide"`)





## Enum: MessageListVisibilityEnum


* `show` (value: `"show"`)

* `hide` (value: `"hide"`)





## Enum: TypeEnum


* `system` (value: `"system"`)

* `user` (value: `"user"`)




