# CallFireApiDocumentation.CallRecording

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callId** | **Number** | An id of a call action | [optional] 
**campaignId** | **Number** | Contains broadcast id if call was sent as a part of voice broadcast | [optional] 
**created** | **Number** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] 
**hash** | **String** | A unique string hash identifier of a recording | [optional] 
**id** | **Number** | An id of a call recording | [optional] 
**lengthInBytes** | **Number** | A size of a recording file in bytes | [optional] 
**lengthInSeconds** | **Number** | Duration of a recording in seconds | [optional] 
**mp3Url** | **String** | A public URL of a call recording | [optional] 
**name** | **String** | A name of a recording | [optional] 
**state** | **String** | Current state of a recording, available values: RECORDING - recording is in progress, READY - recording is ready, ERROR - error has occurred and recording can be broken | [optional] 



## Enum: StateEnum


* `RECORDING` (value: `"RECORDING"`)

* `READY` (value: `"READY"`)

* `ERROR` (value: `"ERROR"`)




