

# PolicySetDefinitionPropertiesParametersValue

The definition of a parameter that can be provided to the policy.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedValues** | **List&lt;Object&gt;** | The allowed values for the parameter. |  [optional] |
|**defaultValue** | **Object** | The default value for the parameter if no value is provided. |  [optional] |
|**metadata** | **Map&lt;String, Object&gt;** | General metadata for the parameter. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The data type of the parameter. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| STRING | &quot;String&quot; |
| ARRAY | &quot;Array&quot; |
| OBJECT | &quot;Object&quot; |
| BOOLEAN | &quot;Boolean&quot; |
| INTEGER | &quot;Integer&quot; |
| FLOAT | &quot;Float&quot; |
| DATE_TIME | &quot;DateTime&quot; |



