

# Label

Labels are used to categorize messages and threads within the user's mailbox. The maximum number of labels supported for a user's mailbox is 10,000.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**color** | [**LabelColor**](LabelColor.md) |  |  [optional] |
|**id** | **String** | The immutable ID of the label. |  [optional] |
|**labelListVisibility** | [**LabelListVisibilityEnum**](#LabelListVisibilityEnum) | The visibility of the label in the label list in the Gmail web interface. |  [optional] |
|**messageListVisibility** | [**MessageListVisibilityEnum**](#MessageListVisibilityEnum) | The visibility of messages with this label in the message list in the Gmail web interface. |  [optional] |
|**messagesTotal** | **Integer** | The total number of messages with the label. |  [optional] |
|**messagesUnread** | **Integer** | The number of unread messages with the label. |  [optional] |
|**name** | **String** | The display name of the label. |  [optional] |
|**threadsTotal** | **Integer** | The total number of threads with the label. |  [optional] |
|**threadsUnread** | **Integer** | The number of unread threads with the label. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The owner type for the label. User labels are created by the user and can be modified and deleted by the user and can be applied to any message or thread. System labels are internally created and cannot be added, modified, or deleted. System labels may be able to be applied to or removed from messages and threads under some circumstances but this is not guaranteed. For example, users can apply and remove the &#x60;INBOX&#x60; and &#x60;UNREAD&#x60; labels from messages and threads, but cannot apply or remove the &#x60;DRAFTS&#x60; or &#x60;SENT&#x60; labels from messages or threads. |  [optional] |



## Enum: LabelListVisibilityEnum

| Name | Value |
|---- | -----|
| LABEL_SHOW | &quot;labelShow&quot; |
| LABEL_SHOW_IF_UNREAD | &quot;labelShowIfUnread&quot; |
| LABEL_HIDE | &quot;labelHide&quot; |



## Enum: MessageListVisibilityEnum

| Name | Value |
|---- | -----|
| SHOW | &quot;show&quot; |
| HIDE | &quot;hide&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;system&quot; |
| USER | &quot;user&quot; |



