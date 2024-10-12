

# GoogleCloudChannelV1ReportJob

The result of a RunReportJob operation. Contains the name to use in FetchReportResultsRequest.report_job and the status of the operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. The resource name of a report job. Name uses the format: &#x60;accounts/{account_id}/reportJobs/{report_job_id}&#x60; |  [optional] |
|**reportStatus** | [**GoogleCloudChannelV1ReportStatus**](GoogleCloudChannelV1ReportStatus.md) |  |  [optional] |



