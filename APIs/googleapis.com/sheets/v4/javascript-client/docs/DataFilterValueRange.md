# GoogleSheetsApi.DataFilterValueRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataFilter** | [**DataFilter**](DataFilter.md) |  | [optional] 
**majorDimension** | **String** | The major dimension of the values. | [optional] 
**values** | **[[Object]]** | The data to be written. If the provided values exceed any of the ranges matched by the data filter then the request fails. If the provided values are less than the matched ranges only the specified values are written, existing values in the matched ranges remain unaffected. | [optional] 



## Enum: MajorDimensionEnum


* `DIMENSION_UNSPECIFIED` (value: `"DIMENSION_UNSPECIFIED"`)

* `ROWS` (value: `"ROWS"`)

* `COLUMNS` (value: `"COLUMNS"`)




