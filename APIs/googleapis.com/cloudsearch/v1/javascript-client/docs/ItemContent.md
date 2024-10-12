# CloudSearchApi.ItemContent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contentDataRef** | [**UploadItemRef**](UploadItemRef.md) |  | [optional] 
**contentFormat** | **String** |  | [optional] 
**hash** | **String** | Hashing info calculated and provided by the API client for content. Can be used with the items.push method to calculate modified state. The maximum length is 2048 characters. | [optional] 
**inlineContent** | **Blob** | Content that is supplied inlined within the update method. The maximum length is 102400 bytes (100 KiB). | [optional] 



## Enum: ContentFormatEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `HTML` (value: `"HTML"`)

* `TEXT` (value: `"TEXT"`)

* `RAW` (value: `"RAW"`)




