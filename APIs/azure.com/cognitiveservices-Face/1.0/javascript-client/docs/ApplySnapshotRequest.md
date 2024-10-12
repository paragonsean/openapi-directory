# FaceClient.ApplySnapshotRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **String** | Snapshot applying mode. Currently only CreateNew is supported, which means the apply operation will fail if target subscription already contains an object of same type and using the same objectId. Users can specify the \&quot;objectId\&quot; in request body to avoid such conflicts. | [optional] [default to &#39;CreateNew&#39;]
**objectId** | **String** | User specified target object id to be created from the snapshot. | 



## Enum: ModeEnum


* `CreateNew` (value: `"CreateNew"`)




