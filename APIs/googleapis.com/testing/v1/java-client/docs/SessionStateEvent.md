

# SessionStateEvent

A message encapsulating a series of Session states and the time that the DeviceSession first entered those states.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**eventTime** | **String** | Output only. The time that the session_state first encountered that state. |  [optional] [readonly] |
|**sessionState** | [**SessionStateEnum**](#SessionStateEnum) | Output only. The session_state tracked by this event |  [optional] [readonly] |
|**stateMessage** | **String** | Output only. A human-readable message to explain the state. |  [optional] [readonly] |



## Enum: SessionStateEnum

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



