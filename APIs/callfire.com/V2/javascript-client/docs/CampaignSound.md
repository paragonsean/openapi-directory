# CallFireApiDocumentation.CampaignSound

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **Number** | The time when the given resource was created, formatted in unix time milliseconds (read only). Example: 1473781817000 for Sat, 05 Jan 1985 14:03:37 GMT | [optional] [readonly] 
**duplicate** | **Boolean** | True if the same sound file exists in a sound library of account | [optional] [readonly] 
**id** | **Number** | An id of a sound file | [optional] 
**lengthInSeconds** | **Number** | Length of a sound in seconds | [optional] [readonly] 
**name** | **String** | A name of a sound file | [optional] 
**status** | **String** | A current status of a sound, available values: UPLOAD - uploading is in progress, RECORDING - recording of sound is in progress, ACTIVE - sound is ready, FAILED, ARCHIVED - sound was archived, SCRUBBED - sound was scrubbed  | [optional] [readonly] 



## Enum: StatusEnum


* `UPLOAD` (value: `"UPLOAD"`)

* `RECORDING` (value: `"RECORDING"`)

* `ACTIVE` (value: `"ACTIVE"`)

* `ACTIVE_SYSTEM` (value: `"ACTIVE_SYSTEM"`)

* `FAILED` (value: `"FAILED"`)

* `ARCHIVED` (value: `"ARCHIVED"`)

* `SCRUBBED` (value: `"SCRUBBED"`)




