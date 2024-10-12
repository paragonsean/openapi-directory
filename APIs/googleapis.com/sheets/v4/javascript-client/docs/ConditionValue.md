# GoogleSheetsApi.ConditionValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**relativeDate** | **String** | A relative date (based on the current date). Valid only if the type is DATE_BEFORE, DATE_AFTER, DATE_ON_OR_BEFORE or DATE_ON_OR_AFTER. Relative dates are not supported in data validation. They are supported only in conditional formatting and conditional filters. | [optional] 
**userEnteredValue** | **String** | A value the condition is based on. The value is parsed as if the user typed into a cell. Formulas are supported (and must begin with an &#x60;&#x3D;&#x60; or a &#39;+&#39;). | [optional] 



## Enum: RelativeDateEnum


* `RELATIVE_DATE_UNSPECIFIED` (value: `"RELATIVE_DATE_UNSPECIFIED"`)

* `PAST_YEAR` (value: `"PAST_YEAR"`)

* `PAST_MONTH` (value: `"PAST_MONTH"`)

* `PAST_WEEK` (value: `"PAST_WEEK"`)

* `YESTERDAY` (value: `"YESTERDAY"`)

* `TODAY` (value: `"TODAY"`)

* `TOMORROW` (value: `"TOMORROW"`)




