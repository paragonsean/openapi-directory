

# PacketCaptureQueryStatusResult

Status of packet capture session.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**captureStartTime** | **OffsetDateTime** | The start time of the packet capture session. |  [optional] |
|**id** | **String** | The ID of the packet capture resource. |  [optional] |
|**name** | **String** | The name of the packet capture resource. |  [optional] |
|**packetCaptureError** | [**List&lt;PacketCaptureErrorEnum&gt;**](#List&lt;PacketCaptureErrorEnum&gt;) | List of errors of packet capture session. |  [optional] |
|**packetCaptureStatus** | [**PacketCaptureStatusEnum**](#PacketCaptureStatusEnum) | The status of the packet capture session. |  [optional] |
|**stopReason** | **String** | The reason the current packet capture session was stopped. |  [optional] |



## Enum: List&lt;PacketCaptureErrorEnum&gt;

| Name | Value |
|---- | -----|
| INTERNAL_ERROR | &quot;InternalError&quot; |
| AGENT_STOPPED | &quot;AgentStopped&quot; |
| CAPTURE_FAILED | &quot;CaptureFailed&quot; |
| LOCAL_FILE_FAILED | &quot;LocalFileFailed&quot; |
| STORAGE_FAILED | &quot;StorageFailed&quot; |



## Enum: PacketCaptureStatusEnum

| Name | Value |
|---- | -----|
| NOT_STARTED | &quot;NotStarted&quot; |
| RUNNING | &quot;Running&quot; |
| STOPPED | &quot;Stopped&quot; |
| ERROR | &quot;Error&quot; |
| UNKNOWN | &quot;Unknown&quot; |



