

# DeviceSession

Protobuf message describing the device message, used from several RPCs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**activeStartTime** | **String** | Output only. The timestamp that the session first became ACTIVE. |  [optional] [readonly] |
|**androidDevice** | [**AndroidDevice**](AndroidDevice.md) |  |  [optional] |
|**createTime** | **String** | Output only. The time that the Session was created. |  [optional] [readonly] |
|**displayName** | **String** | Output only. The title of the DeviceSession to be presented in the UI. |  [optional] [readonly] |
|**expireTime** | **String** | Optional. If the device is still in use at this time, any connections will be ended and the SessionState will transition from ACTIVE to FINISHED. |  [optional] |
|**inactivityTimeout** | **String** | Output only. The interval of time that this device must be interacted with before it transitions from ACTIVE to TIMEOUT_INACTIVITY. |  [optional] [readonly] |
|**name** | **String** | Optional. Name of the DeviceSession, e.g. \&quot;projects/{project_id}/deviceSessions/{session_id}\&quot; |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the DeviceSession. |  [optional] [readonly] |
|**stateHistories** | [**List&lt;SessionStateEvent&gt;**](SessionStateEvent.md) | Output only. The historical state transitions of the session_state message including the current session state. |  [optional] [readonly] |
|**ttl** | **String** | Optional. The amount of time that a device will be initially allocated for. This can eventually be extended with the UpdateDeviceSession RPC. Default: 30 minutes. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| SESSION_STATE_UNSPECIFIED | &quot;SESSION_STATE_UNSPECIFIED&quot; |
| REQUESTED | &quot;REQUESTED&quot; |
| PENDING | &quot;PENDING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| EXPIRED | &quot;EXPIRED&quot; |
| FINISHED | &quot;FINISHED&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |
| ERROR | &quot;ERROR&quot; |



