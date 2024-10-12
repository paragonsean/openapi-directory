

# Field


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alias** | **String** | Alias overrides the field name in the returned response.  Applies only if type is &#x60;func&#x60; |  [optional] |
|**args** | [**List&lt;Field&gt;**](Field.md) | Args are the arguments to the function |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | &#x60;type&#x60; describes the field type. &#x60;func&#x60; is a function. &#x60;field&#x60; is a field reference. |  [optional] |
|**value** | **String** | value is the value of the field.  Meaning of the value is implied by the &#x60;type&#x60; key |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| FUNC | &quot;func&quot; |
| FIELD | &quot;field&quot; |
| INTEGER | &quot;integer&quot; |
| NUMBER | &quot;number&quot; |
| REGEX | &quot;regex&quot; |
| WILDCARD | &quot;wildcard&quot; |



