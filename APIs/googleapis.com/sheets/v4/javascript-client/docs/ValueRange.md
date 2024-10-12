# GoogleSheetsApi.ValueRange

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**majorDimension** | **String** | The major dimension of the values. For output, if the spreadsheet data is: &#x60;A1&#x3D;1,B1&#x3D;2,A2&#x3D;3,B2&#x3D;4&#x60;, then requesting &#x60;range&#x3D;A1:B2,majorDimension&#x3D;ROWS&#x60; will return &#x60;[[1,2],[3,4]]&#x60;, whereas requesting &#x60;range&#x3D;A1:B2,majorDimension&#x3D;COLUMNS&#x60; will return &#x60;[[1,3],[2,4]]&#x60;. For input, with &#x60;range&#x3D;A1:B2,majorDimension&#x3D;ROWS&#x60; then &#x60;[[1,2],[3,4]]&#x60; will set &#x60;A1&#x3D;1,B1&#x3D;2,A2&#x3D;3,B2&#x3D;4&#x60;. With &#x60;range&#x3D;A1:B2,majorDimension&#x3D;COLUMNS&#x60; then &#x60;[[1,2],[3,4]]&#x60; will set &#x60;A1&#x3D;1,B1&#x3D;3,A2&#x3D;2,B2&#x3D;4&#x60;. When writing, if this field is not set, it defaults to ROWS. | [optional] 
**range** | **String** | The range the values cover, in [A1 notation](/sheets/api/guides/concepts#cell). For output, this range indicates the entire requested range, even though the values will exclude trailing rows and columns. When appending values, this field represents the range to search for a table, after which values will be appended. | [optional] 
**values** | **[[Object]]** | The data that was read or to be written. This is an array of arrays, the outer array representing all the data and each inner array representing a major dimension. Each item in the inner array corresponds with one cell. For output, empty trailing rows and columns will not be included. For input, supported value types are: bool, string, and double. Null values will be skipped. To set a cell to an empty value, set the string value to an empty string. | [optional] 



## Enum: MajorDimensionEnum


* `DIMENSION_UNSPECIFIED` (value: `"DIMENSION_UNSPECIFIED"`)

* `ROWS` (value: `"ROWS"`)

* `COLUMNS` (value: `"COLUMNS"`)




