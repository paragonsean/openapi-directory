

# AS2Transport

Describes a single AS2 connection in all of it variations

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentDescription** | **String** | A description of the content of the message. Usually, the same for all messages. |  [optional] |
|**mimeType** | **String** | The MIME type of the message |  [optional] |
|**receiverId** | **String** | The AS2 id of the receiver. Usually, the same for all senders. |  |
|**receiverUrl** | **String** | The URL to the AS2 end-point |  |
|**senderEmail** | **String** | The email address to contact someone about the message |  [optional] |
|**senderId** | **String** | The AS2 id of the sender. Usually, assigned by receiver to PRIME. |  |
|**type** | **String** | The discriminator |  |



