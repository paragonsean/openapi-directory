# CloudLoggingApi.IndexConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The timestamp when the index was last modified.This is used to return the timestamp, and will be ignored if supplied during update. | [optional] [readonly] 
**fieldPath** | **String** | Required. The LogEntry field path to index.Note that some paths are automatically indexed, and other paths are not eligible for indexing. See indexing documentation( https://cloud.google.com/logging/docs/view/advanced-queries#indexed-fields) for details.For example: jsonPayload.request.status | [optional] 
**type** | **String** | Required. The type of data in this index. | [optional] 



## Enum: TypeEnum


* `UNSPECIFIED` (value: `"INDEX_TYPE_UNSPECIFIED"`)

* `STRING` (value: `"INDEX_TYPE_STRING"`)

* `INTEGER` (value: `"INDEX_TYPE_INTEGER"`)




