# GoogleSheetsApi.BatchGetValuesByDataFilterRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataFilters** | [**[DataFilter]**](DataFilter.md) | The data filters used to match the ranges of values to retrieve. Ranges that match any of the specified data filters are included in the response. | [optional] 
**dateTimeRenderOption** | **String** | How dates, times, and durations should be represented in the output. This is ignored if value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER. | [optional] 
**majorDimension** | **String** | The major dimension that results should use. For example, if the spreadsheet data is: &#x60;A1&#x3D;1,B1&#x3D;2,A2&#x3D;3,B2&#x3D;4&#x60;, then a request that selects that range and sets &#x60;majorDimension&#x3D;ROWS&#x60; returns &#x60;[[1,2],[3,4]]&#x60;, whereas a request that sets &#x60;majorDimension&#x3D;COLUMNS&#x60; returns &#x60;[[1,3],[2,4]]&#x60;. | [optional] 
**valueRenderOption** | **String** | How values should be represented in the output. The default render option is FORMATTED_VALUE. | [optional] 



## Enum: DateTimeRenderOptionEnum


* `SERIAL_NUMBER` (value: `"SERIAL_NUMBER"`)

* `FORMATTED_STRING` (value: `"FORMATTED_STRING"`)





## Enum: MajorDimensionEnum


* `DIMENSION_UNSPECIFIED` (value: `"DIMENSION_UNSPECIFIED"`)

* `ROWS` (value: `"ROWS"`)

* `COLUMNS` (value: `"COLUMNS"`)





## Enum: ValueRenderOptionEnum


* `FORMATTED_VALUE` (value: `"FORMATTED_VALUE"`)

* `UNFORMATTED_VALUE` (value: `"UNFORMATTED_VALUE"`)

* `FORMULA` (value: `"FORMULA"`)




