

# SchemaConfig

Configuration for the FHIR BigQuery schema. Determines how the server generates the schema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lastUpdatedPartitionConfig** | [**TimePartitioning**](TimePartitioning.md) |  |  [optional] |
|**recursiveStructureDepth** | **String** | The depth for all recursive structures in the output analytics schema. For example, &#x60;concept&#x60; in the CodeSystem resource is a recursive structure; when the depth is 2, the CodeSystem table will have a column called &#x60;concept.concept&#x60; but not &#x60;concept.concept.concept&#x60;. If not specified or set to 0, the server will use the default value 2. The maximum depth allowed is 5. |  [optional] |
|**schemaType** | [**SchemaTypeEnum**](#SchemaTypeEnum) | Specifies the output schema type. Schema type is required. |  [optional] |



## Enum: SchemaTypeEnum

| Name | Value |
|---- | -----|
| SCHEMA_TYPE_UNSPECIFIED | &quot;SCHEMA_TYPE_UNSPECIFIED&quot; |
| ANALYTICS | &quot;ANALYTICS&quot; |
| ANALYTICS_V2 | &quot;ANALYTICS_V2&quot; |



