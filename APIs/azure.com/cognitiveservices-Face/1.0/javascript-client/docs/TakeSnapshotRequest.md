# FaceClient.TakeSnapshotRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applyScope** | **[String]** | Array of the target Face subscription ids for the snapshot, specified by the user who created the snapshot when calling Snapshot - Take. For each snapshot, only subscriptions included in the applyScope of Snapshot - Take can apply it. | 
**objectId** | **String** | User specified source object id to take snapshot from. | 
**type** | **String** | User specified type for the source object to take snapshot from. Currently FaceList, PersonGroup, LargeFaceList and LargePersonGroup are supported. | 
**userData** | **String** | User specified data about the snapshot for any purpose. Length should not exceed 16KB. | [optional] 



## Enum: TypeEnum


* `FaceList` (value: `"FaceList"`)

* `LargeFaceList` (value: `"LargeFaceList"`)

* `LargePersonGroup` (value: `"LargePersonGroup"`)

* `PersonGroup` (value: `"PersonGroup"`)




