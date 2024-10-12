

# Header

The header information of the columns requested in the report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**currencyCode** | **String** | The [ISO-4217 currency code](https://en.wikipedia.org/wiki/ISO_4217) of this column. Only present if the header type is METRIC_CURRENCY. |  [optional] |
|**name** | **String** | Required. Name of the header. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Type of the header. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| HEADER_TYPE_UNSPECIFIED | &quot;HEADER_TYPE_UNSPECIFIED&quot; |
| DIMENSION | &quot;DIMENSION&quot; |
| METRIC_TALLY | &quot;METRIC_TALLY&quot; |
| METRIC_RATIO | &quot;METRIC_RATIO&quot; |
| METRIC_CURRENCY | &quot;METRIC_CURRENCY&quot; |
| METRIC_MILLISECONDS | &quot;METRIC_MILLISECONDS&quot; |
| METRIC_DECIMAL | &quot;METRIC_DECIMAL&quot; |



