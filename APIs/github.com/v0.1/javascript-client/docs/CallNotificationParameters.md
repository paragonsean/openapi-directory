# EqivoApi.CallNotificationParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aLegRequestUUID** | **String** | A leg call request&#39;s unique identifier | [optional] 
**aLegUUID** | **String** | A leg call&#39;s unique identifier, assigned by FreeSWITCH | [optional] 
**answeredBy** | **String** | Answering actor, when answering machine detection is enabled | [optional] 
**callStatus** | **String** | Call&#39;s current status | 
**callUUID** | **String** | Call&#39;s unique identifier, assigned by FreeSWITCH | 
**callerName** | **String** | Caller name set for the call | 
**coreUUID** | **String** | FreeSWITCH&#39;s instance unique identifier (Eqivo extension) | 
**direction** | **String** | Call&#39;s direction | 
**forwardedFrom** | **String** | Original call destination (before diversion) | [optional] 
**from** | **String** | Caller ID set for the call | 
**machineDetectionDuration** | **Number** | Actual answering machine detection assessment duration (in milliseconds) | [optional] 
**restApiServer** | **String** | Eqivo Rest API server which controls the call (Eqivo extension) | 
**scheduledHangupId** | **String** | Unique identifier of the scheduled hangup task | [optional] 
**to** | **String** | Called phone number | 



## Enum: AnsweredByEnum


* `machine_start` (value: `"machine_start"`)

* `machine_end_beep` (value: `"machine_end_beep"`)

* `machine_end_other` (value: `"machine_end_other"`)

* `human` (value: `"human"`)

* `unknown` (value: `"unknown"`)





## Enum: CallStatusEnum


* `ringing` (value: `"ringing"`)

* `early-media` (value: `"early-media"`)

* `answer` (value: `"answer"`)

* `in-progress` (value: `"in-progress"`)

* `completed` (value: `"completed"`)





## Enum: DirectionEnum


* `inbound` (value: `"inbound"`)

* `outbound` (value: `"outbound"`)




