# CloudTestingApi.SessionStateEvent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventTime** | **String** | Output only. The time that the session_state first encountered that state. | [optional] [readonly] 
**sessionState** | **String** | Output only. The session_state tracked by this event | [optional] [readonly] 
**stateMessage** | **String** | Output only. A human-readable message to explain the state. | [optional] [readonly] 



## Enum: SessionStateEnum


* `SESSION_STATE_UNSPECIFIED` (value: `"SESSION_STATE_UNSPECIFIED"`)

* `REQUESTED` (value: `"REQUESTED"`)

* `PENDING` (value: `"PENDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `EXPIRED` (value: `"EXPIRED"`)

* `FINISHED` (value: `"FINISHED"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)

* `ERROR` (value: `"ERROR"`)




