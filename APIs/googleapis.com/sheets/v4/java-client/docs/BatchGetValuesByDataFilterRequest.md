

# BatchGetValuesByDataFilterRequest

The request for retrieving a range of values in a spreadsheet selected by a set of DataFilters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dataFilters** | [**List&lt;DataFilter&gt;**](DataFilter.md) | The data filters used to match the ranges of values to retrieve. Ranges that match any of the specified data filters are included in the response. |  [optional] |
|**dateTimeRenderOption** | [**DateTimeRenderOptionEnum**](#DateTimeRenderOptionEnum) | How dates, times, and durations should be represented in the output. This is ignored if value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER. |  [optional] |
|**majorDimension** | [**MajorDimensionEnum**](#MajorDimensionEnum) | The major dimension that results should use. For example, if the spreadsheet data is: &#x60;A1&#x3D;1,B1&#x3D;2,A2&#x3D;3,B2&#x3D;4&#x60;, then a request that selects that range and sets &#x60;majorDimension&#x3D;ROWS&#x60; returns &#x60;[[1,2],[3,4]]&#x60;, whereas a request that sets &#x60;majorDimension&#x3D;COLUMNS&#x60; returns &#x60;[[1,3],[2,4]]&#x60;. |  [optional] |
|**valueRenderOption** | [**ValueRenderOptionEnum**](#ValueRenderOptionEnum) | How values should be represented in the output. The default render option is FORMATTED_VALUE. |  [optional] |



## Enum: DateTimeRenderOptionEnum

| Name | Value |
|---- | -----|
| SERIAL_NUMBER | &quot;SERIAL_NUMBER&quot; |
| FORMATTED_STRING | &quot;FORMATTED_STRING&quot; |



## Enum: MajorDimensionEnum

| Name | Value |
|---- | -----|
| DIMENSION_UNSPECIFIED | &quot;DIMENSION_UNSPECIFIED&quot; |
| ROWS | &quot;ROWS&quot; |
| COLUMNS | &quot;COLUMNS&quot; |



## Enum: ValueRenderOptionEnum

| Name | Value |
|---- | -----|
| FORMATTED_VALUE | &quot;FORMATTED_VALUE&quot; |
| UNFORMATTED_VALUE | &quot;UNFORMATTED_VALUE&quot; |
| FORMULA | &quot;FORMULA&quot; |



