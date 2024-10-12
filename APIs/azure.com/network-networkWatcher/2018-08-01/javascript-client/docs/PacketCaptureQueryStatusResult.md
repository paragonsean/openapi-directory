# NetworkManagementClient.PacketCaptureQueryStatusResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**captureStartTime** | **Date** | The start time of the packet capture session. | [optional] 
**id** | **String** | The ID of the packet capture resource. | [optional] 
**name** | **String** | The name of the packet capture resource. | [optional] 
**packetCaptureError** | **[String]** | List of errors of packet capture session. | [optional] 
**packetCaptureStatus** | **String** | The status of the packet capture session. | [optional] 
**stopReason** | **String** | The reason the current packet capture session was stopped. | [optional] 



## Enum: [PacketCaptureErrorEnum]


* `InternalError` (value: `"InternalError"`)

* `AgentStopped` (value: `"AgentStopped"`)

* `CaptureFailed` (value: `"CaptureFailed"`)

* `LocalFileFailed` (value: `"LocalFileFailed"`)

* `StorageFailed` (value: `"StorageFailed"`)





## Enum: PacketCaptureStatusEnum


* `NotStarted` (value: `"NotStarted"`)

* `Running` (value: `"Running"`)

* `Stopped` (value: `"Stopped"`)

* `Error` (value: `"Error"`)

* `Unknown` (value: `"Unknown"`)




