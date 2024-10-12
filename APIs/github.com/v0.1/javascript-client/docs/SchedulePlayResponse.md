# EqivoApi.SchedulePlayResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **String** | Response message | 
**schedPlayId** | **String** | Unique identifier of the scheduled playback request (UUIDv4) | 
**success** | **Boolean** | Whether the request was successful or not | 



## Enum: MessageEnum


* `Play Executed` (value: `"Play Executed"`)

* `CallUUID Parameter Missing` (value: `"CallUUID Parameter Missing"`)

* `Sounds Parameter Missing` (value: `"Sounds Parameter Missing"`)

* `Time Parameter Missing` (value: `"Time Parameter Missing"`)

* `Time Parameter must be &gt; 0` (value: `"Time Parameter must be > 0"`)

* `Legs Parameter is Invalid` (value: `"Legs Parameter is Invalid"`)

* `Length Parameter must be a positive integer` (value: `"Length Parameter must be a positive integer"`)

* `Sounds Parameter is Invalid` (value: `"Sounds Parameter is Invalid"`)

* `Play Failed -- Call not found` (value: `"Play Failed -- Call not found"`)

* `Play Failed` (value: `"Play Failed"`)




