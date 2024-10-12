

# History

A record of a change to the user's mailbox. Each history change may affect multiple messages in multiple ways.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | The mailbox sequence ID. |  [optional] |
|**labelsAdded** | [**List&lt;HistoryLabelAdded&gt;**](HistoryLabelAdded.md) | Labels added to messages in this history record. |  [optional] |
|**labelsRemoved** | [**List&lt;HistoryLabelRemoved&gt;**](HistoryLabelRemoved.md) | Labels removed from messages in this history record. |  [optional] |
|**messages** | [**List&lt;Message&gt;**](Message.md) | List of messages changed in this history record. The fields for specific change types, such as &#x60;messagesAdded&#x60; may duplicate messages in this field. We recommend using the specific change-type fields instead of this. |  [optional] |
|**messagesAdded** | [**List&lt;HistoryMessageAdded&gt;**](HistoryMessageAdded.md) | Messages added to the mailbox in this history record. |  [optional] |
|**messagesDeleted** | [**List&lt;HistoryMessageDeleted&gt;**](HistoryMessageDeleted.md) | Messages deleted (not Trashed) from the mailbox in this history record. |  [optional] |



