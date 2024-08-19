

# Call


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **Long** | Unique identifier of the account |  |
|**answerTime** | **LocalDate** | Time to answer the call |  [optional] |
|**callerId** | **String** | Remote caller ID |  [optional] |
|**direction** | [**DirectionEnum**](#DirectionEnum) | Direction of the call |  |
|**duration** | **Long** | Duration of the call in milliseconds |  |
|**endTime** | **LocalDate** | End time of the call |  [optional] |
|**externalId** | **String** | External identifier of the call |  [optional] |
|**id** | **Long** | Unique identifier of the call |  |
|**phoneNumber** | **String** | Unique identifier of the account |  |
|**startTime** | **LocalDate** | Start time of the call |  |
|**state** | [**StateEnum**](#StateEnum) | Status of the call |  |
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



