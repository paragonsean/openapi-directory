

# NumberFormat

The number format of a cell.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**pattern** | **String** | Pattern string used for formatting. If not set, a default pattern based on the user&#39;s locale will be used if necessary for the given type. See the [Date and Number Formats guide](/sheets/api/guides/formats) for more information about the supported patterns. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of the number format. When writing, this field must be set. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NUMBER_FORMAT_TYPE_UNSPECIFIED | &quot;NUMBER_FORMAT_TYPE_UNSPECIFIED&quot; |
| TEXT | &quot;TEXT&quot; |
| NUMBER | &quot;NUMBER&quot; |
| PERCENT | &quot;PERCENT&quot; |
| CURRENCY | &quot;CURRENCY&quot; |
| DATE | &quot;DATE&quot; |
| TIME | &quot;TIME&quot; |
| DATE_TIME | &quot;DATE_TIME&quot; |
| SCIENTIFIC | &quot;SCIENTIFIC&quot; |



