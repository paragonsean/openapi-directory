

# AppRestrictionsSchemaRestrictionRestrictionValue

A typed value for the restriction.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of the value being provided. |  [optional] |
|**valueBool** | **Boolean** | The boolean value - this will only be present if type is bool. |  [optional] |
|**valueInteger** | **Integer** | The integer value - this will only be present if type is integer. |  [optional] |
|**valueMultiselect** | **List&lt;String&gt;** | The list of string values - this will only be present if type is multiselect. |  [optional] |
|**valueString** | **String** | The string value - this will be present for types string, choice and hidden. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| BOOL | &quot;bool&quot; |
| STRING | &quot;string&quot; |
| INTEGER | &quot;integer&quot; |
| CHOICE | &quot;choice&quot; |
| MULTISELECT | &quot;multiselect&quot; |
| HIDDEN | &quot;hidden&quot; |
| BUNDLE | &quot;bundle&quot; |
| BUNDLE_ARRAY | &quot;bundleArray&quot; |



