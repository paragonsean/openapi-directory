

# DataSourceParameter

A parameter used to define custom fields in a data source definition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedValues** | **List&lt;String&gt;** | All possible values for the parameter. |  [optional] |
|**deprecated** | **Boolean** | If true, it should not be used in new transfers, and it should not be visible to users. |  [optional] |
|**description** | **String** | Parameter description. |  [optional] |
|**displayName** | **String** | Parameter display name in the user interface. |  [optional] |
|**fields** | [**List&lt;DataSourceParameter&gt;**](DataSourceParameter.md) | Deprecated. This field has no effect. |  [optional] |
|**immutable** | **Boolean** | Cannot be changed after initial creation. |  [optional] |
|**maxValue** | **Double** | For integer and double values specifies maximum allowed value. |  [optional] |
|**minValue** | **Double** | For integer and double values specifies minimum allowed value. |  [optional] |
|**paramId** | **String** | Parameter identifier. |  [optional] |
|**recurse** | **Boolean** | Deprecated. This field has no effect. |  [optional] |
|**repeated** | **Boolean** | Deprecated. This field has no effect. |  [optional] |
|**required** | **Boolean** | Is parameter required. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Parameter type. |  [optional] |
|**validationDescription** | **String** | Description of the requirements for this field, in case the user input does not fulfill the regex pattern or min/max values. |  [optional] |
|**validationHelpUrl** | **String** | URL to a help document to further explain the naming requirements. |  [optional] |
|**validationRegex** | **String** | Regular expression which can be used for parameter validation. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| STRING | &quot;STRING&quot; |
| INTEGER | &quot;INTEGER&quot; |
| DOUBLE | &quot;DOUBLE&quot; |
| BOOLEAN | &quot;BOOLEAN&quot; |
| RECORD | &quot;RECORD&quot; |
| PLUS_PAGE | &quot;PLUS_PAGE&quot; |
| LIST | &quot;LIST&quot; |



