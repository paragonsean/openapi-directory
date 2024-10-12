

# StandardHL7ConfigurationTransport


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filePath** | **String** | The file path to place the report |  |
|**host** | **String** | Host name and domain |  |
|**port** | **BigDecimal** | The port to use |  |
|**type** | **String** | The discriminator |  |
|**contentDescription** | **String** | A description of the content of the message. Usually, the same for all messages. |  [optional] |
|**mimeType** | **String** | The MIME type of the message |  [optional] |
|**receiverId** | **String** | The AS2 id of the receiver. Usually, the same for all senders. |  |
|**receiverUrl** | **String** | The URL to the AS2 end-point |  |
|**senderEmail** | **String** | The email address to contact someone about the message |  [optional] |
|**senderId** | **String** | The AS2 id of the sender. Usually, assigned by receiver to PRIME. |  |
|**containerName** | **String** | This name of the Azure container |  |
|**storageName** | **String** | This looks for an env var with this name. env var value is the connection string |  |
|**dummy** | **String** | A dummy value |  [optional] |



