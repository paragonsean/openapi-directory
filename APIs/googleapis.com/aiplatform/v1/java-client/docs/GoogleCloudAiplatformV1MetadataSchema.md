

# GoogleCloudAiplatformV1MetadataSchema

Instance of a general MetadataSchema.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. Timestamp when this MetadataSchema was created. |  [optional] [readonly] |
|**description** | **String** | Description of the Metadata Schema |  [optional] |
|**name** | **String** | Output only. The resource name of the MetadataSchema. |  [optional] [readonly] |
|**schema** | **String** | Required. The raw YAML string representation of the MetadataSchema. The combination of [MetadataSchema.version] and the schema name given by &#x60;title&#x60; in [MetadataSchema.schema] must be unique within a MetadataStore. The schema is defined as an OpenAPI 3.0.2 [MetadataSchema Object](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2.md#schemaObject) |  [optional] |
|**schemaType** | [**SchemaTypeEnum**](#SchemaTypeEnum) | The type of the MetadataSchema. This is a property that identifies which metadata types will use the MetadataSchema. |  [optional] |
|**schemaVersion** | **String** | The version of the MetadataSchema. The version&#39;s format must match the following regular expression: &#x60;^[0-9]+.+.+$&#x60;, which would allow to order/compare different versions. Example: 1.0.0, 1.0.1, etc. |  [optional] |



## Enum: SchemaTypeEnum

| Name | Value |
|---- | -----|
| METADATA_SCHEMA_TYPE_UNSPECIFIED | &quot;METADATA_SCHEMA_TYPE_UNSPECIFIED&quot; |
| ARTIFACT_TYPE | &quot;ARTIFACT_TYPE&quot; |
| EXECUTION_TYPE | &quot;EXECUTION_TYPE&quot; |
| CONTEXT_TYPE | &quot;CONTEXT_TYPE&quot; |



