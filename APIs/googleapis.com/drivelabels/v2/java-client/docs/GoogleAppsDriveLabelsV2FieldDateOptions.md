

# GoogleAppsDriveLabelsV2FieldDateOptions

Options for the date field type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dateFormat** | **String** | Output only. ICU date format. |  [optional] [readonly] |
|**dateFormatType** | [**DateFormatTypeEnum**](#DateFormatTypeEnum) | Localized date formatting option. Field values are rendered in this format according to their locale. |  [optional] |
|**maxValue** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |
|**minValue** | [**GoogleTypeDate**](GoogleTypeDate.md) |  |  [optional] |



## Enum: DateFormatTypeEnum

| Name | Value |
|---- | -----|
| DATE_FORMAT_UNSPECIFIED | &quot;DATE_FORMAT_UNSPECIFIED&quot; |
| LONG_DATE | &quot;LONG_DATE&quot; |
| SHORT_DATE | &quot;SHORT_DATE&quot; |



