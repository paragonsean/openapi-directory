

# ReconciliationReportValidationIssue

Represents an issue encountered when validating a reconciliation report.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | Text description of the issue, typically including what was seen and why it was invalid. |  [optional] |
|**fieldName** | **String** | Name of the invalid field. If no field name is given, this issue applies to the whole line (or file). |  [optional] |
|**lineNum** | **Integer** | The line number on which the issue was detected. If this field is 0, the issue applies to the whole file. |  [optional] |



