# SensitiveDataProtectionDlp.GooglePrivacyDlpV2BigQueryOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**excludedFields** | [**[GooglePrivacyDlpV2FieldId]**](GooglePrivacyDlpV2FieldId.md) | References to fields excluded from scanning. This allows you to skip inspection of entire columns which you know have no findings. When inspecting a table, we recommend that you inspect all columns. Otherwise, findings might be affected because hints from excluded columns will not be used. | [optional] 
**identifyingFields** | [**[GooglePrivacyDlpV2FieldId]**](GooglePrivacyDlpV2FieldId.md) | Table fields that may uniquely identify a row within the table. When &#x60;actions.saveFindings.outputConfig.table&#x60; is specified, the values of columns specified here are available in the output table under &#x60;location.content_locations.record_location.record_key.id_values&#x60;. Nested fields such as &#x60;person.birthdate.year&#x60; are allowed. | [optional] 
**includedFields** | [**[GooglePrivacyDlpV2FieldId]**](GooglePrivacyDlpV2FieldId.md) | Limit scanning only to these fields. When inspecting a table, we recommend that you inspect all columns. Otherwise, findings might be affected because hints from excluded columns will not be used. | [optional] 
**rowsLimit** | **String** | Max number of rows to scan. If the table has more rows than this value, the rest of the rows are omitted. If not set, or if set to 0, all rows will be scanned. Only one of rows_limit and rows_limit_percent can be specified. Cannot be used in conjunction with TimespanConfig. | [optional] 
**rowsLimitPercent** | **Number** | Max percentage of rows to scan. The rest are omitted. The number of rows scanned is rounded down. Must be between 0 and 100, inclusively. Both 0 and 100 means no limit. Defaults to 0. Only one of rows_limit and rows_limit_percent can be specified. Cannot be used in conjunction with TimespanConfig. Caution: A [known issue](https://cloud.google.com/sensitive-data-protection/docs/known-issues#bq-sampling) is causing the &#x60;rowsLimitPercent&#x60; field to behave unexpectedly. We recommend using &#x60;rowsLimit&#x60; instead. | [optional] 
**sampleMethod** | **String** | How to sample the data. | [optional] 
**tableReference** | [**GooglePrivacyDlpV2BigQueryTable**](GooglePrivacyDlpV2BigQueryTable.md) |  | [optional] 



## Enum: SampleMethodEnum


* `SAMPLE_METHOD_UNSPECIFIED` (value: `"SAMPLE_METHOD_UNSPECIFIED"`)

* `TOP` (value: `"TOP"`)

* `RANDOM_START` (value: `"RANDOM_START"`)




