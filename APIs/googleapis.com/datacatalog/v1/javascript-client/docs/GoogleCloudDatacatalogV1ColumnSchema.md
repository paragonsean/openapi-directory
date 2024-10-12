# GoogleCloudDataCatalogApi.GoogleCloudDatacatalogV1ColumnSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column** | **String** | Required. Name of the column. Must be a UTF-8 string without dots (.). The maximum size is 64 bytes. | [optional] 
**defaultValue** | **String** | Optional. Default value for the column. | [optional] 
**description** | **String** | Optional. Description of the column. Default value is an empty string. The description must be a UTF-8 string with the maximum size of 2000 bytes. | [optional] 
**gcRule** | **String** | Optional. Garbage collection policy for the column or column family. Applies to systems like Cloud Bigtable. | [optional] 
**highestIndexingType** | **String** | Optional. Most important inclusion of this column. | [optional] 
**lookerColumnSpec** | [**GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpec**](GoogleCloudDatacatalogV1ColumnSchemaLookerColumnSpec.md) |  | [optional] 
**mode** | **String** | Optional. A column&#39;s mode indicates whether values in this column are required, nullable, or repeated. Only &#x60;NULLABLE&#x60;, &#x60;REQUIRED&#x60;, and &#x60;REPEATED&#x60; values are supported. Default mode is &#x60;NULLABLE&#x60;. | [optional] 
**ordinalPosition** | **Number** | Optional. Ordinal position | [optional] 
**rangeElementType** | [**GoogleCloudDatacatalogV1ColumnSchemaFieldElementType**](GoogleCloudDatacatalogV1ColumnSchemaFieldElementType.md) |  | [optional] 
**subcolumns** | [**[GoogleCloudDatacatalogV1ColumnSchema]**](GoogleCloudDatacatalogV1ColumnSchema.md) | Optional. Schema of sub-columns. A column can have zero or more sub-columns. | [optional] 
**type** | **String** | Required. Type of the column. Must be a UTF-8 string with the maximum size of 128 bytes. | [optional] 



## Enum: HighestIndexingTypeEnum


* `UNSPECIFIED` (value: `"INDEXING_TYPE_UNSPECIFIED"`)

* `NONE` (value: `"INDEXING_TYPE_NONE"`)

* `NON_UNIQUE` (value: `"INDEXING_TYPE_NON_UNIQUE"`)

* `UNIQUE` (value: `"INDEXING_TYPE_UNIQUE"`)

* `PRIMARY_KEY` (value: `"INDEXING_TYPE_PRIMARY_KEY"`)




