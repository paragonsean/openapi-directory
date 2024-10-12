# CloudSearchApi.ItemStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Status code. | [optional] 
**processingErrors** | [**[ProcessingError]**](ProcessingError.md) | Error details in case the item is in ERROR state. | [optional] 
**repositoryErrors** | [**[RepositoryError]**](RepositoryError.md) | Repository error reported by connector. | [optional] 



## Enum: CodeEnum


* `CODE_UNSPECIFIED` (value: `"CODE_UNSPECIFIED"`)

* `ERROR` (value: `"ERROR"`)

* `MODIFIED` (value: `"MODIFIED"`)

* `NEW_ITEM` (value: `"NEW_ITEM"`)

* `ACCEPTED` (value: `"ACCEPTED"`)




