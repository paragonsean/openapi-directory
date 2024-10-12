

# FieldReference

Reference definition to use with field overrides.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateFormat** | [**DateFormatEnum**](#DateFormatEnum) | Only valid if the &#x60;fieldPath&#x60; references a date field. Chooses how the date field will be formatted and displayed in the UI. |  [optional] |
|**fieldPath** | **String** | Path to the field being referenced, prefixed with \&quot;object\&quot; or \&quot;class\&quot; and separated with dots. For example, it may be the string \&quot;object.purchaseDetails.purchasePrice\&quot;. |  [optional] |



## Enum: DateFormatEnum

| Name | Value |
|---- | -----|
| DATE_FORMAT_UNSPECIFIED | &quot;DATE_FORMAT_UNSPECIFIED&quot; |
| DATE_TIME | &quot;DATE_TIME&quot; |
| DATE_TIME2 | &quot;dateTime&quot; |
| DATE_ONLY | &quot;DATE_ONLY&quot; |
| DATE_ONLY2 | &quot;dateOnly&quot; |
| TIME_ONLY | &quot;TIME_ONLY&quot; |
| TIME_ONLY2 | &quot;timeOnly&quot; |
| DATE_TIME_YEAR | &quot;DATE_TIME_YEAR&quot; |
| DATE_TIME_YEAR2 | &quot;dateTimeYear&quot; |
| DATE_YEAR | &quot;DATE_YEAR&quot; |
| DATE_YEAR2 | &quot;dateYear&quot; |
| YEAR_MONTH | &quot;YEAR_MONTH&quot; |
| YEAR_MONTH_DAY | &quot;YEAR_MONTH_DAY&quot; |



