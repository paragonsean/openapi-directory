# GoogleSheetsApi.NumberFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pattern** | **String** | Pattern string used for formatting. If not set, a default pattern based on the user&#39;s locale will be used if necessary for the given type. See the [Date and Number Formats guide](/sheets/api/guides/formats) for more information about the supported patterns. | [optional] 
**type** | **String** | The type of the number format. When writing, this field must be set. | [optional] 



## Enum: TypeEnum


* `NUMBER_FORMAT_TYPE_UNSPECIFIED` (value: `"NUMBER_FORMAT_TYPE_UNSPECIFIED"`)

* `TEXT` (value: `"TEXT"`)

* `NUMBER` (value: `"NUMBER"`)

* `PERCENT` (value: `"PERCENT"`)

* `CURRENCY` (value: `"CURRENCY"`)

* `DATE` (value: `"DATE"`)

* `TIME` (value: `"TIME"`)

* `DATE_TIME` (value: `"DATE_TIME"`)

* `SCIENTIFIC` (value: `"SCIENTIFIC"`)




