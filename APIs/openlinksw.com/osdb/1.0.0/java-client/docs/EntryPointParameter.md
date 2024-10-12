

# EntryPointParameter


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A short description of the parameter for use in the OSDB Action Console. Optional - may be null. |  |
|**displayName** | **String** | The parameter&#39;s display name in the OSDB Action Console. Optional - may be null. |  |
|**parameterName** | **String** | The parameter name as present in the HTTP request. e.g. the key name in a query string key-value pair. |  |
|**permittedValues** | **List&lt;String&gt;** | If the parameter accepts only a limited set of values, the allowed set of values. Null if not applicable. |  |
|**required** | **Integer** | A flag indicating if the parameter is optional. |  |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the parameter, indicating its location in the HTTP request. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| QUERY | &quot;query&quot; |
| HEADER | &quot;header&quot; |
| URI | &quot;uri&quot; |
| PATH | &quot;path&quot; |
| BODY | &quot;body&quot; |



