# AnchoreEngineApiServer.GroupSyncResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **String** | The name of the group | [optional] 
**status** | **String** |  | [optional] 
**totalTimeSeconds** | **Number** | The duration of the group sync in seconds | [optional] 
**updatedImageCount** | **Number** | The number of images updated by the this group sync, across all accounts. This is typically only non-zero for vulnerability feeds which update images&#39; vulnerability results during the sync. | [optional] 
**updatedRecordCount** | **Number** | The number of feed data records synced down as either updates or new records | [optional] 



## Enum: StatusEnum


* `success` (value: `"success"`)

* `failure` (value: `"failure"`)




