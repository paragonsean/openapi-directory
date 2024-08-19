# VonageIntegrationSuite.Call

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **Number** | Unique identifier of the account | 
**answerTime** | **Date** | Time to answer the call | [optional] 
**callerId** | **String** | Remote caller ID | [optional] 
**direction** | **String** | Direction of the call | 
**duration** | **Number** | Duration of the call in milliseconds | 
**endTime** | **Date** | End time of the call | [optional] 
**externalId** | **String** | External identifier of the call | [optional] 
**id** | **Number** | Unique identifier of the call | 
**phoneNumber** | **String** | Unique identifier of the account | 
**startTime** | **Date** | Start time of the call | 
**state** | **String** | Status of the call | 
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




