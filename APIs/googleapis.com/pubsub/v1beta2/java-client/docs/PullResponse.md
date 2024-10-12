

# PullResponse

Response for the `Pull` method.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**receivedMessages** | [**List&lt;ReceivedMessage&gt;**](ReceivedMessage.md) | Received Pub/Sub messages. The Pub/Sub system will return zero messages if there are no more available in the backlog. The Pub/Sub system may return fewer than the &#x60;maxMessages&#x60; requested even if there are more messages available in the backlog. |  [optional] |



