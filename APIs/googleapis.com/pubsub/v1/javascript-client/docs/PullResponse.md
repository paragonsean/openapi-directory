# CloudPubSubApi.PullResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**receivedMessages** | [**[ReceivedMessage]**](ReceivedMessage.md) | Optional. Received Pub/Sub messages. The list will be empty if there are no more messages available in the backlog, or if no messages could be returned before the request timeout. For JSON, the response can be entirely empty. The Pub/Sub system may return fewer than the &#x60;maxMessages&#x60; requested even if there are more messages available in the backlog. | [optional] 


