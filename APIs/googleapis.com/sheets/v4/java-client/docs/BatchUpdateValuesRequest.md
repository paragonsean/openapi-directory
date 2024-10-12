

# BatchUpdateValuesRequest

The request for updating more than one range of values in a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;ValueRange&gt;**](ValueRange.md) | The new values to apply to the spreadsheet. |  [optional] |
|**includeValuesInResponse** | **Boolean** | Determines if the update response should include the values of the cells that were updated. By default, responses do not include the updated values. The &#x60;updatedData&#x60; field within each of the BatchUpdateValuesResponse.responses contains the updated values. If the range to write was larger than the range actually written, the response includes all values in the requested range (excluding trailing empty rows and columns). |  [optional] |
|**responseDateTimeRenderOption** | [**ResponseDateTimeRenderOptionEnum**](#ResponseDateTimeRenderOptionEnum) | Determines how dates, times, and durations in the response should be rendered. This is ignored if response_value_render_option is FORMATTED_VALUE. The default dateTime render option is SERIAL_NUMBER. |  [optional] |
|**responseValueRenderOption** | [**ResponseValueRenderOptionEnum**](#ResponseValueRenderOptionEnum) | Determines how values in the response should be rendered. The default render option is FORMATTED_VALUE. |  [optional] |
|**valueInputOption** | [**ValueInputOptionEnum**](#ValueInputOptionEnum) | How the input data should be interpreted. |  [optional] |



## Enum: ResponseDateTimeRenderOptionEnum

| Name | Value |
|---- | -----|
| SERIAL_NUMBER | &quot;SERIAL_NUMBER&quot; |
| FORMATTED_STRING | &quot;FORMATTED_STRING&quot; |



## Enum: ResponseValueRenderOptionEnum

| Name | Value |
|---- | -----|
| FORMATTED_VALUE | &quot;FORMATTED_VALUE&quot; |
| UNFORMATTED_VALUE | &quot;UNFORMATTED_VALUE&quot; |
| FORMULA | &quot;FORMULA&quot; |



## Enum: ValueInputOptionEnum

| Name | Value |
|---- | -----|
| INPUT_VALUE_OPTION_UNSPECIFIED | &quot;INPUT_VALUE_OPTION_UNSPECIFIED&quot; |
| RAW | &quot;RAW&quot; |
| USER_ENTERED | &quot;USER_ENTERED&quot; |



