# DracoonApi.CompleteUploadRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fileKey** | [**FileKey**](FileKey.md) |  | [optional] 
**fileName** | **String** | New file name to store with | [optional] 
**keepShareLinks** | **Boolean** | Preserve Download Share Links and point them to the new node. | [optional] [default to false]
**resolutionStrategy** | **String** | Node conflict resolution strategy:  * &#x60;autorename&#x60;  * &#x60;overwrite&#x60;  * &#x60;fail&#x60; | [optional] [default to &#39;autorename&#39;]
**userFileKeyList** | [**UserFileKeyList**](UserFileKeyList.md) |  | [optional] 



## Enum: ResolutionStrategyEnum


* `autorename` (value: `"autorename"`)

* `overwrite` (value: `"overwrite"`)

* `fail` (value: `"fail"`)




