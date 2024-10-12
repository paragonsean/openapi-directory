# CloudMonitoringApi.LabelDescriptor

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **String** | A human-readable description for the label. | [optional] 
**key** | **String** | The key for this label. The key must meet the following criteria: Does not exceed 100 characters. Matches the following regular expression: [a-zA-Z][a-zA-Z0-9_]* The first character must be an upper- or lower-case letter. The remaining characters must be letters, digits, or underscores. | [optional] 
**valueType** | **String** | The type of data that can be assigned to the label. | [optional] 



## Enum: ValueTypeEnum


* `STRING` (value: `"STRING"`)

* `BOOL` (value: `"BOOL"`)

* `INT64` (value: `"INT64"`)




