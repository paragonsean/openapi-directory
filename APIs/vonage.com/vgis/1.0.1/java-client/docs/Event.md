

# Event


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Long** | Unique identifier of the account |  |
|**answerTime** | **LocalDate** | Time to answer the event |  [optional] |
|**callerId** | **String** | Remote caller ID |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | Direction of the event |  |
|**duration** | **Long** | Duration of the call in milliseconds |  [optional] |
|**endTime** | **LocalDate** | End time of the event |  [optional] |
|**externalId** | **String** | External identifier of the event |  [optional] |
|**id** | **Long** | Unique identifier of the event |  |
|**phoneNumber** | **String** | Unique identifier of the account |  |
|**smsData** | **String** |  |  [optional] |
|**startTime** | **LocalDate** | Start time of the event |  |
|**state** | [**StateEnum**](#StateEnum) | Status of the event |  |
|**type** | [**TypeEnum**](#TypeEnum) | Record type |  |
|**uciId** | **Long** | Unique identifier of communications provider |  |
|**userId** | **Long** | Unique identifier of the user |  |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| INBOUND | &quot;INBOUND&quot; |
| OUTBOUND | &quot;OUTBOUND&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| INITIALIZING | &quot;INITIALIZING&quot; |
| RINGING | &quot;RINGING&quot; |
| ACTIVE | &quot;ACTIVE&quot; |
| HELD | &quot;HELD&quot; |
| REMOTE_HELD | &quot;REMOTE_HELD&quot; |
| DETACHED | &quot;DETACHED&quot; |
| REJECTED | &quot;REJECTED&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| ANSWERED | &quot;ANSWERED&quot; |
| MISSED | &quot;MISSED&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| CALL | &quot;CALL&quot; |



