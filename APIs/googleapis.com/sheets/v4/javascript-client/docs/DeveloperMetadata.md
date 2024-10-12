# GoogleSheetsApi.DeveloperMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | [**DeveloperMetadataLocation**](DeveloperMetadataLocation.md) |  | [optional] 
**metadataId** | **Number** | The spreadsheet-scoped unique ID that identifies the metadata. IDs may be specified when metadata is created, otherwise one will be randomly generated and assigned. Must be positive. | [optional] 
**metadataKey** | **String** | The metadata key. There may be multiple metadata in a spreadsheet with the same key. Developer metadata must always have a key specified. | [optional] 
**metadataValue** | **String** | Data associated with the metadata&#39;s key. | [optional] 
**visibility** | **String** | The metadata visibility. Developer metadata must always have a visibility specified. | [optional] 



## Enum: VisibilityEnum


* `DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED` (value: `"DEVELOPER_METADATA_VISIBILITY_UNSPECIFIED"`)

* `DOCUMENT` (value: `"DOCUMENT"`)

* `PROJECT` (value: `"PROJECT"`)




