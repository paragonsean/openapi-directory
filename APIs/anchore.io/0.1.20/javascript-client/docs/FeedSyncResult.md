# AnchoreEngineApiServer.FeedSyncResult

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feed** | **String** | The name of the feed synced | [optional] 
**groups** | [**[GroupSyncResult]**](GroupSyncResult.md) | Array of group sync results | [optional] 
**status** | **String** | The result of the sync operations, either co | [optional] 
**totalTimeSeconds** | **Number** | The duratin, in seconds, of the sync of the feed, the sum of all the group syncs | [optional] 



## Enum: StatusEnum


* `success` (value: `"success"`)

* `failure` (value: `"failure"`)




