

# SourceNumericFilter

Filter for fixed point number data types such as NUMERIC/NUMBER

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**numericFilterOption** | [**NumericFilterOptionEnum**](#NumericFilterOptionEnum) | Required. Enum to set the option defining the datatypes numeric filter has to be applied to |  [optional] |
|**sourceMaxPrecisionFilter** | **Integer** | Optional. The filter will match columns with precision smaller than or equal to this number. |  [optional] |
|**sourceMaxScaleFilter** | **Integer** | Optional. The filter will match columns with scale smaller than or equal to this number. |  [optional] |
|**sourceMinPrecisionFilter** | **Integer** | Optional. The filter will match columns with precision greater than or equal to this number. |  [optional] |
|**sourceMinScaleFilter** | **Integer** | Optional. The filter will match columns with scale greater than or equal to this number. |  [optional] |



## Enum: NumericFilterOptionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;NUMERIC_FILTER_OPTION_UNSPECIFIED&quot; |
| ALL | &quot;NUMERIC_FILTER_OPTION_ALL&quot; |
| LIMIT | &quot;NUMERIC_FILTER_OPTION_LIMIT&quot; |
| LIMITLESS | &quot;NUMERIC_FILTER_OPTION_LIMITLESS&quot; |



