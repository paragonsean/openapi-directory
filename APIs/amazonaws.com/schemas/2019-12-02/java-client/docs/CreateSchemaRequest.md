

# CreateSchemaRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **String** | The source of the schema definition. |  |
|**description** | **String** | A description of the schema. |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Key-value pairs associated with a resource. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of schema. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OPEN_API3 | &quot;OpenApi3&quot; |
| JSON_SCHEMA_DRAFT4 | &quot;JSONSchemaDraft4&quot; |



