

# QueueMessage

A Queue Message

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentType** | **String** | Content-type of data associated with QueueMessage. |  [optional] |
|**createDate** | **Long** | Date that message was received by system. |  [optional] |
|**data** | **String** | Embedded JSON to be sent with Queue Message. |  [optional] |
|**href** | **String** | URL of data associated with Queue Message (if not embedded JSON) |  [optional] |
|**messageId** | **UUID** | UUID of Message Data associated with this Queue Message |  [optional] |
|**queueMessageId** | **UUID** | UUID of Queue Message in local region. |  [optional] |
|**queueName** | **String** | Name of Queue for message. |  |
|**receivingRegion** | **String** | Regions to which message will be sent |  [optional] |
|**sendingRegion** | **String** | Region from which was sent |  [optional] |



