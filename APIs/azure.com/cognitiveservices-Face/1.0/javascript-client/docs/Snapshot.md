# FaceClient.Snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account** | **String** | Azure Cognitive Service Face account id of the subscriber who created the snapshot by Snapshot - Take. | 
**applyScope** | **[String]** | Array of the target Face subscription ids for the snapshot, specified by the user who created the snapshot when calling Snapshot - Take. For each snapshot, only subscriptions included in the applyScope of Snapshot - Take can apply it. | 
**createdTime** | **Date** | A combined UTC date and time string that describes the created time of the snapshot. E.g. 2018-12-25T11:41:02.2331413Z. | 
**id** | **String** | Snapshot id. | 
**lastUpdateTime** | **Date** | A combined UTC date and time string that describes the last time when the snapshot was created or updated by Snapshot - Update. E.g. 2018-12-25T11:51:27.8705696Z. | 
**type** | **String** | Type of the source object in the snapshot, specified by the subscriber who created the snapshot when calling Snapshot - Take. Currently FaceList, PersonGroup, LargeFaceList and LargePersonGroup are supported. | 
**userData** | **String** | User specified data about the snapshot for any purpose. Length should not exceed 16KB. | [optional] 



## Enum: TypeEnum


* `FaceList` (value: `"FaceList"`)

* `LargeFaceList` (value: `"LargeFaceList"`)

* `LargePersonGroup` (value: `"LargePersonGroup"`)

* `PersonGroup` (value: `"PersonGroup"`)




