

# DeveloperMetadata

Developer metadata associated with a location or object in a spreadsheet. Developer metadata may be used to associate arbitrary data with various parts of a spreadsheet and will remain associated at those locations as they move around and the spreadsheet is edited. For example, if developer metadata is associated with row 5 and another row is then subsequently inserted above row 5, that original metadata will still be associated with the row it was first associated with (what is now row 6). If the associated object is deleted its metadata is deleted too.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | [**DeveloperMetadataLocation**](DeveloperMetadataLocation.md) |  |  [optional] |
|**metadataId** | **Integer** | The spreadsheet-scoped unique ID that identifies the metadata. IDs may be specified when metadata is created, otherwise one will be randomly generated and assigned. Must be positive. |  [optional] |
|**metadataKey** | **String** | The metadata key. There may be multiple metadata in a spreadsheet with the same key. Developer metadata must always have a key specified. |  [optional] |
|**metadataValue** | **String** | Data associated with the metadata&#39;s key. |  [optional] |
|**visibility** | [**VisibilityEnum**](#VisibilityEnum) | The metadata visibility. Developer metadata must always have a visibility specified. |  [optional] |



## Enum: VisibilityEnum

| Name | Value |
|---- | -----|
| DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED | &quot;DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED&quot; |
| DOCUMENT | &quot;DOCUMENT&quot; |
| PROJECT | &quot;PROJECT&quot; |



