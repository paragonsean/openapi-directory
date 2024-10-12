# WowzaStreamingCloudRestApiReferenceDocumentation.Recording

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdAt** | **Date** | The date and time that the recording was created. | [optional] 
**downloadUrl** | **String** | The URL that can be used to download the recording. | [optional] 
**duration** | **Number** | The length of the recording, in hours, minutes, and seconds. | [optional] 
**fileName** | **String** | The file name of the recording. | [optional] 
**fileSize** | **Number** | The file size of the recording. | [optional] 
**id** | **String** | The unique alphanumeric string that identifies the recording. | [optional] 
**reason** | **String** | The reason that a recording has the state &lt;strong&gt;failed&lt;/strong&gt;. | [optional] 
**startsAt** | **String** | The date and time that the recording started. | [optional] 
**state** | **String** | The state of the recording. | [optional] 
**transcoderId** | **String** | The unique alphanumeric string that identifies the transcoder that was recorded. | [optional] 
**transcoderName** | **String** | The descriptive name of the transcoder that was recorded. | [optional] 
**transcodingUptimeId** | **Date** | The unique identifier associated with the transcoding uptime for this recording. | [optional] 
**updatedAt** | **Date** | The date and time that the recording was updated. | [optional] 



## Enum: StateEnum


* `uploading` (value: `"uploading"`)

* `converting` (value: `"converting"`)

* `removing` (value: `"removing"`)

* `completed` (value: `"completed"`)

* `failed` (value: `"failed"`)




