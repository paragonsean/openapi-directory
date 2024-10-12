

# GoogleCloudDocumentaiV1beta1DocumentTextAnchorTextSegment

A text segment in the Document.text. The indices may be out of bounds which indicate that the text extends into another document shard for large sharded documents. See ShardInfo.text_offset

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endIndex** | **String** | TextSegment half open end UTF-8 char index in the Document.text. |  [optional] |
|**startIndex** | **String** | TextSegment start UTF-8 char index in the Document.text. |  [optional] |



