

# CallNotificationParameters


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alegRequestUUID** | **String** | A leg call request&#39;s unique identifier |  [optional] |
|**alegUUID** | **String** | A leg call&#39;s unique identifier, assigned by FreeSWITCH |  [optional] |
|**answeredBy** | [**AnsweredByEnum**](#AnsweredByEnum) | Answering actor, when answering machine detection is enabled |  [optional] |
|**callStatus** | [**CallStatusEnum**](#CallStatusEnum) | Call&#39;s current status |  |
|**callUUID** | **String** | Call&#39;s unique identifier, assigned by FreeSWITCH |  |
|**callerName** | **String** | Caller name set for the call |  |
|**coreUUID** | **String** | FreeSWITCH&#39;s instance unique identifier (Eqivo extension) |  |
|**direction** | [**DirectionEnum**](#DirectionEnum) | Call&#39;s direction |  |
|**forwardedFrom** | **String** | Original call destination (before diversion) |  [optional] |
|**from** | **String** | Caller ID set for the call |  |
|**machineDetectionDuration** | **Integer** | Actual answering machine detection assessment duration (in milliseconds) |  [optional] |
|**restApiServer** | **String** | Eqivo Rest API server which controls the call (Eqivo extension) |  |
|**scheduledHangupId** | **String** | Unique identifier of the scheduled hangup task |  [optional] |
|**to** | **String** | Called phone number |  |



## Enum: AnsweredByEnum

| Name | Value |
|---- | -----|
| MACHINE_START | &quot;machine_start&quot; |
| MACHINE_END_BEEP | &quot;machine_end_beep&quot; |
| MACHINE_END_OTHER | &quot;machine_end_other&quot; |
| HUMAN | &quot;human&quot; |
| UNKNOWN | &quot;unknown&quot; |



## Enum: CallStatusEnum

| Name | Value |
|---- | -----|
| RINGING | &quot;ringing&quot; |
| EARLY_MEDIA | &quot;early-media&quot; |
| ANSWER | &quot;answer&quot; |
| IN_PROGRESS | &quot;in-progress&quot; |
| COMPLETED | &quot;completed&quot; |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;inbound&quot; |
| OUTBOUND | &quot;outbound&quot; |



