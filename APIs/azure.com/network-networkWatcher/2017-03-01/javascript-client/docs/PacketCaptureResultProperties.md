# NetworkManagementClient.PacketCaptureResultProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provisioningState** | **String** | The provisioning state of the packet capture session. | [optional] 
**bytesToCapturePerPacket** | **Number** | Number of bytes captured per packet, the remaining bytes are truncated. | [optional] 
**filters** | [**[PacketCaptureFilter]**](PacketCaptureFilter.md) |  | [optional] 
**storageLocation** | [**PacketCaptureStorageLocation**](PacketCaptureStorageLocation.md) |  | 
**target** | **String** | The ID of the targeted resource, only VM is currently supported. | 
**timeLimitInSeconds** | **Number** | Maximum duration of the capture session in seconds. | [optional] 
**totalBytesPerSession** | **Number** | Maximum size of the capture output. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




