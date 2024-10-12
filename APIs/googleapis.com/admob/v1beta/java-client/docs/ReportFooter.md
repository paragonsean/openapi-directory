

# ReportFooter

Groups data available after report generation, for example, warnings and row counts. Always sent as the last message in the stream response.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**matchingRowCount** | **String** | Total number of rows that matched the request. Warning: This count does NOT always match the number of rows in the response. Do not make that assumption when processing the response. |  [optional] |
|**warnings** | [**List&lt;ReportWarning&gt;**](ReportWarning.md) | Warnings associated with generation of the report. |  [optional] |



