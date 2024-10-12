

# ParameterDefinition

Represent a parameter with constrains and metadata.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedValues** | **List&lt;Object&gt;** | Array of allowed values for this parameter. |  [optional] |
|**defaultValue** | **Object** | Default Value for this parameter. |  [optional] |
|**metadata** | [**ParameterDefinitionMetadata**](ParameterDefinitionMetadata.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Allowed data types for Resource Manager template parameters. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;string&quot; |
| ARRAY | &quot;array&quot; |
| BOOL | &quot;bool&quot; |
| INT | &quot;int&quot; |
| OBJECT | &quot;object&quot; |
| SECURE_OBJECT | &quot;secureObject&quot; |
| SECURE_STRING | &quot;secureString&quot; |



