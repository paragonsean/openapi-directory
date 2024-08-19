

# ScheduleHangupResponse


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**message** | [**MessageEnum**](#MessageEnum) | Response message |  |
|**schedHangupId** | **String** | Unique identifier of the scheduled hangup request (UUIDv4) |  |
|**success** | **Boolean** | Whether the request was successful or not |  |



## Enum: MessageEnum

| Name | Value |
|---- | -----|
| SCHEDULE_HANGUP_EXECUTED | &quot;ScheduleHangup Executed&quot; |
| CALL_UUID_PARAMETER_MUST_BE_PRESENT | &quot;CallUUID Parameter must be present&quot; |
| TIME_PARAMETER_MUST_BE_PRESENT | &quot;Time Parameter must be present&quot; |
| TIME_PARAMETER_MUST_BE_0_ | &quot;Time Parameter must be &gt; 0!&quot; |
| SCHEDULE_HANGUP_FAILED_CALL_NOT_FOUND | &quot;ScheduleHangup Failed -- Call not found&quot; |
| SCHEDULE_HANGUP_FAILED | &quot;ScheduleHangup Failed&quot; |



