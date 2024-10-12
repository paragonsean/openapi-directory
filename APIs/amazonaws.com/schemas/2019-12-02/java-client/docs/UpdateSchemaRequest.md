

# UpdateSchemaRequest


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**clientTokenId** | **String** | The ID of the client token. |  [optional] |
|**content** | **String** | The source of the schema definition. |  [optional] |
|**description** | **String** | The description of the schema. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The schema type for the events schema. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| OPEN_API3 | &quot;OpenApi3&quot; |
| JSON_SCHEMA_DRAFT4 | &quot;JSONSchemaDraft4&quot; |



