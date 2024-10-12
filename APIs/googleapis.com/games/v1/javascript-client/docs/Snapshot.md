# GooglePlayGameServices.Snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coverImage** | [**SnapshotImage**](SnapshotImage.md) |  | [optional] 
**description** | **String** | The description of this snapshot. | [optional] 
**driveId** | **String** | The ID of the file underlying this snapshot in the Drive API. Only present if the snapshot is a view on a Drive file and the file is owned by the caller. | [optional] 
**durationMillis** | **String** | The duration associated with this snapshot, in millis. | [optional] 
**id** | **String** | The ID of the snapshot. | [optional] 
**kind** | **String** | Uniquely identifies the type of this resource. Value is always the fixed string &#x60;games#snapshot&#x60;. | [optional] 
**lastModifiedMillis** | **String** | The timestamp (in millis since Unix epoch) of the last modification to this snapshot. | [optional] 
**progressValue** | **String** | The progress value (64-bit integer set by developer) associated with this snapshot. | [optional] 
**title** | **String** | The title of this snapshot. | [optional] 
**type** | **String** | The type of this snapshot. | [optional] 
**uniqueName** | **String** | The unique name provided when the snapshot was created. | [optional] 



## Enum: TypeEnum


* `SAVE_GAME` (value: `"SAVE_GAME"`)




