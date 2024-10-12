

# Item

Represents a single object that is an item in the search index, such as a file, folder, or a database record.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acl** | [**ItemAcl**](ItemAcl.md) |  |  [optional] |
|**content** | [**ItemContent**](ItemContent.md) |  |  [optional] |
|**itemType** | [**ItemTypeEnum**](#ItemTypeEnum) | The type for this item. |  [optional] |
|**metadata** | [**ItemMetadata**](ItemMetadata.md) |  |  [optional] |
|**name** | **String** | The name of the Item. Format: datasources/{source_id}/items/{item_id} This is a required field. The maximum length is 1536 characters. |  [optional] |
|**payload** | **byte[]** | Additional state connector can store for this item. The maximum length is 10000 bytes. |  [optional] |
|**queue** | **String** | Queue this item belongs to. The maximum length is 100 characters. |  [optional] |
|**status** | [**ItemStatus**](ItemStatus.md) |  |  [optional] |
|**structuredData** | [**ItemStructuredData**](ItemStructuredData.md) |  |  [optional] |
|**version** | **byte[]** | Required. The indexing system stores the version from the datasource as a byte string and compares the Item version in the index to the version of the queued Item using lexical ordering. Cloud Search Indexing won&#39;t index or delete any queued item with a version value that is less than or equal to the version of the currently indexed item. The maximum length for this field is 1024 bytes. For information on how item version affects the deletion process, refer to [Handle revisions after manual deletes](https://developers.google.com/cloud-search/docs/guides/operations). |  [optional] |



## Enum: ItemTypeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| CONTENT_ITEM | &quot;CONTENT_ITEM&quot; |
| CONTAINER_ITEM | &quot;CONTAINER_ITEM&quot; |
| VIRTUAL_CONTAINER_ITEM | &quot;VIRTUAL_CONTAINER_ITEM&quot; |



