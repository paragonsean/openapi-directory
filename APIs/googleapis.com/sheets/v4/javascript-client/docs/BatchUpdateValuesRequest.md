# GoogleSheetsApi.BatchUpdateValuesRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**[ValueRange]**](ValueRange.md) | The new values to apply to the spreadsheet. | [optional] 
**includeValuesInResponse** | **Boolean** | Determines if the update response should include the values of the cells that were updated. By default, responses do not include the updated values. The &#x60;updatedData&#x60; field within each of the BatchUpdateValuesResponse.responses contains the updated values. If the range to write was larger than the range actually written, the response includes all values in the requested range (excluding trailing empty rows and columns). | [optional] 
**responseDateTimeRenderOption** | **String** | Determines how dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER. | [optional] 
**responseValueRenderOption** | **String** | Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE. | [optional] 
**valueInputOption** | **String** | How the input data should be interpreted. | [optional] 



## Enum: ResponseDateTimeRenderOptionEnum


* `SERIAL_NUMBER` (value: `"SERIAL_NUMBER"`)

* `FORMATTED_STRING` (value: `"FORMATTED_STRING"`)





## Enum: ResponseValueRenderOptionEnum


* `FORMATTED_VALUE` (value: `"FORMATTED_VALUE"`)

* `UNFORMATTED_VALUE` (value: `"UNFORMATTED_VALUE"`)

* `FORMULA` (value: `"FORMULA"`)





## Enum: ValueInputOptionEnum


* `INPUT_VALUE_OPTION_UNSPECIFIED` (value: `"INPUT_VALUE_OPTION_UNSPECIFIED"`)

* `RAW` (value: `"RAW"`)

* `USER_ENTERED` (value: `"USER_ENTERED"`)




