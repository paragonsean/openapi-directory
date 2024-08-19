

# PacketCaptureParameters

Parameters that define the create packet capture operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bytesToCapturePerPacket** | **Integer** | Number of bytes captured per packet, the remaining bytes are truncated. |  [optional] |
|**filters** | [**List&lt;PacketCaptureFilter&gt;**](PacketCaptureFilter.md) | A list of packet capture filters. |  [optional] |
|**storageLocation** | [**PacketCaptureStorageLocation**](PacketCaptureStorageLocation.md) |  |  |
|**target** | **String** | The ID of the targeted resource, only VM is currently supported. |  |
|**timeLimitInSeconds** | **Integer** | Maximum duration of the capture session in seconds. |  [optional] |
|**totalBytesPerSession** | **Integer** | Maximum size of the capture output. |  [optional] |



