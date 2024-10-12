# EqivoApi.ScheduleHangupResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Response message | 
**schedHangupId** | **String** | Unique identifier of the scheduled hangup request (UUIDv4) | 
**success** | **Boolean** | Whether the request was successful or not | 



## Enum: MessageEnum


* `ScheduleHangup Executed` (value: `"ScheduleHangup Executed"`)

* `CallUUID Parameter must be present` (value: `"CallUUID Parameter must be present"`)

* `Time Parameter must be present` (value: `"Time Parameter must be present"`)

* `Time Parameter must be &gt; 0!` (value: `"Time Parameter must be > 0!"`)

* `ScheduleHangup Failed -- Call not found` (value: `"ScheduleHangup Failed -- Call not found"`)

* `ScheduleHangup Failed` (value: `"ScheduleHangup Failed"`)




