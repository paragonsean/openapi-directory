# CloudDataplexApi.GoogleCloudDataplexV1ActionIncompatibleDataSchema

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**existingSchema** | **String** | The existing and expected schema of the table. The schema is provided as a JSON formatted structure listing columns and data types. | [optional] 
**newSchema** | **String** | The new and incompatible schema within the table. The schema is provided as a JSON formatted structured listing columns and data types. | [optional] 
**sampledDataLocations** | **[String]** | The list of data locations sampled and used for format/schema inference. | [optional] 
**schemaChange** | **String** | Whether the action relates to a schema that is incompatible or modified. | [optional] 
**table** | **String** | The name of the table containing invalid data. | [optional] 



## Enum: SchemaChangeEnum


* `SCHEMA_CHANGE_UNSPECIFIED` (value: `"SCHEMA_CHANGE_UNSPECIFIED"`)

* `INCOMPATIBLE` (value: `"INCOMPATIBLE"`)

* `MODIFIED` (value: `"MODIFIED"`)




