

# SpreadsheetProperties

Properties of a spreadsheet.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoRecalc** | [**AutoRecalcEnum**](#AutoRecalcEnum) | The amount of time to wait before volatile functions are recalculated. |  [optional] |
|**defaultFormat** | [**CellFormat**](CellFormat.md) |  |  [optional] |
|**iterativeCalculationSettings** | [**IterativeCalculationSettings**](IterativeCalculationSettings.md) |  |  [optional] |
|**locale** | **String** | The locale of the spreadsheet in one of the following formats: * an ISO 639-1 language code such as &#x60;en&#x60; * an ISO 639-2 language code such as &#x60;fil&#x60;, if no 639-1 code exists * a combination of the ISO language code and country code, such as &#x60;en_US&#x60; Note: when updating this field, not all locales/languages are supported. |  [optional] |
|**spreadsheetTheme** | [**SpreadsheetTheme**](SpreadsheetTheme.md) |  |  [optional] |
|**timeZone** | **String** | The time zone of the spreadsheet, in CLDR format such as &#x60;America/New_York&#x60;. If the time zone isn&#39;t recognized, this may be a custom time zone such as &#x60;GMT-07:00&#x60;. |  [optional] |
|**title** | **String** | The title of the spreadsheet. |  [optional] |



## Enum: AutoRecalcEnum

| Name | Value |
|---- | -----|
| RECALCULATION_INTERVAL_UNSPECIFIED | &quot;RECALCULATION_INTERVAL_UNSPECIFIED&quot; |
| ON_CHANGE | &quot;ON_CHANGE&quot; |
| MINUTE | &quot;MINUTE&quot; |
| HOUR | &quot;HOUR&quot; |



