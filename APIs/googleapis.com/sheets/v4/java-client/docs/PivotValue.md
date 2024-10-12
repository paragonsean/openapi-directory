

# PivotValue

The definition of how a value in a pivot table should be calculated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calculatedDisplayType** | [**CalculatedDisplayTypeEnum**](#CalculatedDisplayTypeEnum) | If specified, indicates that pivot values should be displayed as the result of a calculation with another pivot value. For example, if calculated_display_type is specified as PERCENT_OF_GRAND_TOTAL, all the pivot values are displayed as the percentage of the grand total. In the Sheets editor, this is referred to as \&quot;Show As\&quot; in the value section of a pivot table. |  [optional] |
|**dataSourceColumnReference** | [**DataSourceColumnReference**](DataSourceColumnReference.md) |  |  [optional] |
|**formula** | **String** | A custom formula to calculate the value. The formula must start with an &#x60;&#x3D;&#x60; character. |  [optional] |
|**name** | **String** | A name to use for the value. |  [optional] |
|**sourceColumnOffset** | **Integer** | The column offset of the source range that this value reads from. For example, if the source was &#x60;C10:E15&#x60;, a &#x60;sourceColumnOffset&#x60; of &#x60;0&#x60; means this value refers to column &#x60;C&#x60;, whereas the offset &#x60;1&#x60; would refer to column &#x60;D&#x60;. |  [optional] |
|**summarizeFunction** | [**SummarizeFunctionEnum**](#SummarizeFunctionEnum) | A function to summarize the value. If formula is set, the only supported values are SUM and CUSTOM. If sourceColumnOffset is set, then &#x60;CUSTOM&#x60; is not supported. |  [optional] |



## Enum: CalculatedDisplayTypeEnum

| Name | Value |
|---- | -----|
| PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED | &quot;PIVOT_VALUE_CALCULATED_DISPLAY_TYPE_UNSPECIFIED&quot; |
| PERCENT_OF_ROW_TOTAL | &quot;PERCENT_OF_ROW_TOTAL&quot; |
| PERCENT_OF_COLUMN_TOTAL | &quot;PERCENT_OF_COLUMN_TOTAL&quot; |
| PERCENT_OF_GRAND_TOTAL | &quot;PERCENT_OF_GRAND_TOTAL&quot; |



## Enum: SummarizeFunctionEnum

| Name | Value |
|---- | -----|
| PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED | &quot;PIVOT_STANDARD_VALUE_FUNCTION_UNSPECIFIED&quot; |
| SUM | &quot;SUM&quot; |
| COUNTA | &quot;COUNTA&quot; |
| COUNT | &quot;COUNT&quot; |
| COUNTUNIQUE | &quot;COUNTUNIQUE&quot; |
| AVERAGE | &quot;AVERAGE&quot; |
| MAX | &quot;MAX&quot; |
| MIN | &quot;MIN&quot; |
| MEDIAN | &quot;MEDIAN&quot; |
| PRODUCT | &quot;PRODUCT&quot; |
| STDEV | &quot;STDEV&quot; |
| STDEVP | &quot;STDEVP&quot; |
| VAR | &quot;VAR&quot; |
| VARP | &quot;VARP&quot; |
| CUSTOM | &quot;CUSTOM&quot; |



