

# MessageHeader

It conveys Information related to the Sale to POI protocol management. Message header of the Sale to POI protocol message.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deviceID** | **String** | If Device MessageClass. |  [optional] |
|**messageCategory** | **MessageCategory** |  |  |
|**messageClass** | **MessageClass** |  |  |
|**messageType** | **MessageType** |  |  |
|**POIID** | **String** | Identification of a POI System or a POI Terminal for the Sale to POI protocol. |  |
|**protocolVersion** | **String** | If MessageCategory is Login or Diagnosis. |  [optional] |
|**saleID** | **String** | Identification of a Sale System or a Sale Terminal for the Sale to POI protocol. |  |
|**serviceID** | **String** | Required if Service or Event MessageClass message or if Device MessageClass and request from POI or response from Sale. |  [optional] |



