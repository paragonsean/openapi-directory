

# CreateReconciliationReportResponse

Response message for ReconciliationReportService.CreateReconciliationReport.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**issues** | [**List&lt;ReconciliationReportValidationIssue&gt;**](ReconciliationReportValidationIssue.md) | Issues that were encountered when validating the file. |  [optional] |
|**reconciliationReport** | [**ReconciliationReport**](ReconciliationReport.md) |  |  [optional] |
|**successfulRecordCount** | **Integer** | The number of commission records that were successfully saved. |  [optional] |



