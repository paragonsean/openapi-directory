

# PacketCaptureResultProperties

Describes the properties of a packet capture session.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**bytesToCapturePerPacket** | **Integer** | Number of bytes captured per packet, the remaining bytes are truncated. |  [optional] |
|**filters** | [**List&lt;PacketCaptureFilter&gt;**](PacketCaptureFilter.md) | A list of packet capture filters. |  [optional] |
|**storageLocation** | [**PacketCaptureStorageLocation**](PacketCaptureStorageLocation.md) |  |  |
|**target** | **String** | The ID of the targeted resource, only VM is currently supported. |  |
|**timeLimitInSeconds** | **Integer** | Maximum duration of the capture session in seconds. |  [optional] |
|**totalBytesPerSession** | **Integer** | Maximum size of the capture output. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



