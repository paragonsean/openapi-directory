

# DataType

Indicated the type of data that can be stored in a structured data entity (e.g. a table).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**listElementType** | [**DataType**](DataType.md) |  |  [optional] |
|**nullable** | **Boolean** | If true, this DataType can also be &#x60;NULL&#x60;. In .CSV files &#x60;NULL&#x60; value is expressed as an empty string. |  [optional] |
|**structType** | [**StructType**](StructType.md) |  |  [optional] |
|**timeFormat** | **String** | If type_code &#x3D;&#x3D; TIMESTAMP then &#x60;time_format&#x60; provides the format in which that time field is expressed. The time_format must either be one of: * &#x60;UNIX_SECONDS&#x60; * &#x60;UNIX_MILLISECONDS&#x60; * &#x60;UNIX_MICROSECONDS&#x60; * &#x60;UNIX_NANOSECONDS&#x60; (for respectively number of seconds, milliseconds, microseconds and nanoseconds since start of the Unix epoch); or be written in &#x60;strftime&#x60; syntax. If time_format is not set, then the default format as described on the type_code is used. |  [optional] |
|**typeCode** | [**TypeCodeEnum**](#TypeCodeEnum) | Required. The TypeCode for this type. |  [optional] |



## Enum: TypeCodeEnum

| Name | Value |
|---- | -----|
| TYPE_CODE_UNSPECIFIED | &quot;TYPE_CODE_UNSPECIFIED&quot; |
| FLOAT64 | &quot;FLOAT64&quot; |
| TIMESTAMP | &quot;TIMESTAMP&quot; |
| STRING | &quot;STRING&quot; |
| ARRAY | &quot;ARRAY&quot; |
| STRUCT | &quot;STRUCT&quot; |
| CATEGORY | &quot;CATEGORY&quot; |



