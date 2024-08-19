# VonageIntegrationSuite.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **Number** | Unique identifier of the account | 
**answerTime** | **Date** | Time to answer the event | [optional] 
**callerId** | **String** | Remote caller ID | [optional] 
**direction** | **String** | Direction of the event | 
**duration** | **Number** | Duration of the call in milliseconds | [optional] 
**endTime** | **Date** | End time of the event | [optional] 
**externalId** | **String** | External identifier of the event | [optional] 
**id** | **Number** | Unique identifier of the event | 
**phoneNumber** | **String** | Unique identifier of the account | 
**smsData** | **String** |  | [optional] 
**startTime** | **Date** | Start time of the event | 
**state** | **String** | Status of the event | 
**type** | **String** | Record type | 
**uciId** | **Number** | Unique identifier of communications provider | 
**userId** | **Number** | Unique identifier of the user | 



## Enum: DirectionEnum


* `INBOUND` (value: `"INBOUND"`)

* `OUTBOUND` (value: `"OUTBOUND"`)





## Enum: StateEnum


* `INITIALIZING` (value: `"INITIALIZING"`)

* `RINGING` (value: `"RINGING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `HELD` (value: `"HELD"`)

* `REMOTE_HELD` (value: `"REMOTE_HELD"`)

* `DETACHED` (value: `"DETACHED"`)

* `REJECTED` (value: `"REJECTED"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `ANSWERED` (value: `"ANSWERED"`)

* `MISSED` (value: `"MISSED"`)





## Enum: TypeEnum


* `CALL` (value: `"CALL"`)




