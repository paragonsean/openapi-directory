

# MessageReference

To abort a transaction in progress or to request the status of a transaction from which no response has been received.  It identifies the message header of the message request to abort or request the status. Identification of a previous POI transaction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceID** | **String** | Identification of a device message pair. |  [optional] |
|**messageCategory** | **MessageCategory** |  |  [optional] |
|**POIID** | **String** | default MessageHeader.POIID. |  [optional] |
|**saleID** | **String** | default MessageHeader.SaleID. |  [optional] |
|**serviceID** | **String** | Identification of a message pair, which processes a transaction. |  [optional] |



