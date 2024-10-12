# GmailApi.ListMessagesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**[Message]**](Message.md) | List of messages. Note that each message resource contains only an &#x60;id&#x60; and a &#x60;threadId&#x60;. Additional message details can be fetched using the messages.get method. | [optional] 
**nextPageToken** | **String** | Token to retrieve the next page of results in the list. | [optional] 
**resultSizeEstimate** | **Number** | Estimated total number of results. | [optional] 


