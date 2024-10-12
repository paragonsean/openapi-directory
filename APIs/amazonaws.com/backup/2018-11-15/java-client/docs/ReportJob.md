

# ReportJob

Contains detailed information about a report job. A report job compiles a report based on a report plan and publishes it to Amazon S3.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**reportJobId** | [**String**](String.md) |  |  [optional] |
|**reportPlanArn** | [**String**](String.md) |  |  [optional] |
|**reportTemplate** | [**String**](String.md) |  |  [optional] |
|**creationTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**completionTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**status** | [**String**](String.md) |  |  [optional] |
|**statusMessage** | [**String**](String.md) |  |  [optional] |
|**reportDestination** | [**ReportJobReportDestination**](ReportJobReportDestination.md) |  |  [optional] |



