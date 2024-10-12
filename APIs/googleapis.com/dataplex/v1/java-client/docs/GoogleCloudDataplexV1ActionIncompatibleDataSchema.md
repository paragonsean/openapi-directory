

# GoogleCloudDataplexV1ActionIncompatibleDataSchema

Action details for incompatible schemas detected by discovery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**existingSchema** | **String** | The existing and expected schema of the table. The schema is provided as a JSON formatted structure listing columns and data types. |  [optional] |
|**newSchema** | **String** | The new and incompatible schema within the table. The schema is provided as a JSON formatted structured listing columns and data types. |  [optional] |
|**sampledDataLocations** | **List&lt;String&gt;** | The list of data locations sampled and used for format/schema inference. |  [optional] |
|**schemaChange** | [**SchemaChangeEnum**](#SchemaChangeEnum) | Whether the action relates to a schema that is incompatible or modified. |  [optional] |
|**table** | **String** | The name of the table containing invalid data. |  [optional] |



## Enum: SchemaChangeEnum

| Name | Value |
|---- | -----|
| SCHEMA_CHANGE_UNSPECIFIED | &quot;SCHEMA_CHANGE_UNSPECIFIED&quot; |
| INCOMPATIBLE | &quot;INCOMPATIBLE&quot; |
| MODIFIED | &quot;MODIFIED&quot; |



