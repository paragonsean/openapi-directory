# CloudSearchApi.ItemCountByStatus

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **String** | Number of items matching the status code. | [optional] 
**indexedItemsCount** | **String** | Number of items matching the status code for which billing is done. This excludes virtual container items from the total count. This count would not be applicable for items with ERROR or NEW_ITEM status code. | [optional] 
**statusCode** | **String** | Status of the items. | [optional] 



## Enum: StatusCodeEnum


* `CODE_UNSPECIFIED` (value: `"CODE_UNSPECIFIED"`)

* `ERROR` (value: `"ERROR"`)

* `MODIFIED` (value: `"MODIFIED"`)

* `NEW_ITEM` (value: `"NEW_ITEM"`)

* `ACCEPTED` (value: `"ACCEPTED"`)




