

# DeleteMessageRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**id** | **String** | ID of the message to be deleted. This is the &lt;code&gt;Id&lt;/code&gt; field in the received message (see &lt;a href&#x3D;\&quot;https://docs.aws.amazon.com/ivs/latest/chatmsgapireference/actions-message-subscribe.html\&quot;&gt; Message (Subscribe)&lt;/a&gt; in the Chat Messaging API). |  |
|**reason** | **String** | Reason for deleting the message. |  [optional] |
|**roomIdentifier** | **String** | Identifier of the room where the message should be deleted. Currently this must be an ARN.  |  |



