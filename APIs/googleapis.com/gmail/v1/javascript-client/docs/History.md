# GmailApi.History

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The mailbox sequence ID. | [optional] 
**labelsAdded** | [**[HistoryLabelAdded]**](HistoryLabelAdded.md) | Labels added to messages in this history record. | [optional] 
**labelsRemoved** | [**[HistoryLabelRemoved]**](HistoryLabelRemoved.md) | Labels removed from messages in this history record. | [optional] 
**messages** | [**[Message]**](Message.md) | List of messages changed in this history record. The fields for specific change types, such as &#x60;messagesAdded&#x60; may duplicate messages in this field. We recommend using the specific change-type fields instead of this. | [optional] 
**messagesAdded** | [**[HistoryMessageAdded]**](HistoryMessageAdded.md) | Messages added to the mailbox in this history record. | [optional] 
**messagesDeleted** | [**[HistoryMessageDeleted]**](HistoryMessageDeleted.md) | Messages deleted (not Trashed) from the mailbox in this history record. | [optional] 


