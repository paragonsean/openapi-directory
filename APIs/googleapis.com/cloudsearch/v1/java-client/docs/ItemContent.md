

# ItemContent

Content of an item to be indexed and surfaced by Cloud Search. Only UTF-8 encoded strings are allowed as inlineContent. If the content is uploaded and not binary, it must be UTF-8 encoded.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**contentDataRef** | [**UploadItemRef**](UploadItemRef.md) |  |  [optional] |
|**contentFormat** | [**ContentFormatEnum**](#ContentFormatEnum) |  |  [optional] |
|**hash** | **String** | Hashing info calculated and provided by the API client for content. Can be used with the items.push method to calculate modified state. The maximum length is 2048 characters. |  [optional] |
|**inlineContent** | **byte[]** | Content that is supplied inlined within the update method. The maximum length is 102400 bytes (100 KiB). |  [optional] |



## Enum: ContentFormatEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| HTML | &quot;HTML&quot; |
| TEXT | &quot;TEXT&quot; |
| RAW | &quot;RAW&quot; |



