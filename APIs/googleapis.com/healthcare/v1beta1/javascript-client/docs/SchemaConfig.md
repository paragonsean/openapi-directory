# CloudHealthcareApi.SchemaConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lastUpdatedPartitionConfig** | [**TimePartitioning**](TimePartitioning.md) |  | [optional] 
**recursiveStructureDepth** | **String** | The depth for all recursive structures in the output analytics schema. For example, &#x60;concept&#x60; in the CodeSystem resource is a recursive structure; when the depth is 2, the CodeSystem table will have a column called &#x60;concept.concept&#x60; but not &#x60;concept.concept.concept&#x60;. If not specified or set to 0, the server will use the default value 2. The maximum depth allowed is 5. | [optional] 
**schemaType** | **String** | Specifies the output schema type. Schema type is required. | [optional] 



## Enum: SchemaTypeEnum


* `SCHEMA_TYPE_UNSPECIFIED` (value: `"SCHEMA_TYPE_UNSPECIFIED"`)

* `LOSSLESS` (value: `"LOSSLESS"`)

* `ANALYTICS` (value: `"ANALYTICS"`)

* `ANALYTICS_V2` (value: `"ANALYTICS_V2"`)




