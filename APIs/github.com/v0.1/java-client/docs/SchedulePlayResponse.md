

# SchedulePlayResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**MessageEnum**](#MessageEnum) | Response message |  |
|**schedPlayId** | **String** | Unique identifier of the scheduled playback request (UUIDv4) |  |
|**success** | **Boolean** | Whether the request was successful or not |  |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| PLAY_EXECUTED | &quot;Play Executed&quot; |
| CALL_UUID_PARAMETER_MISSING | &quot;CallUUID Parameter Missing&quot; |
| SOUNDS_PARAMETER_MISSING | &quot;Sounds Parameter Missing&quot; |
| TIME_PARAMETER_MISSING | &quot;Time Parameter Missing&quot; |
| TIME_PARAMETER_MUST_BE_0 | &quot;Time Parameter must be &gt; 0&quot; |
| LEGS_PARAMETER_IS_INVALID | &quot;Legs Parameter is Invalid&quot; |
| LENGTH_PARAMETER_MUST_BE_A_POSITIVE_INTEGER | &quot;Length Parameter must be a positive integer&quot; |
| SOUNDS_PARAMETER_IS_INVALID | &quot;Sounds Parameter is Invalid&quot; |
| PLAY_FAILED_CALL_NOT_FOUND | &quot;Play Failed -- Call not found&quot; |
| PLAY_FAILED | &quot;Play Failed&quot; |



