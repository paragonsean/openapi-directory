

# Report

Information about the results from running a series of test cases during the run of a build project. The test cases are specified in the buildspec for the build project using one or more paths to the test case files. You can specify any type of tests you want, such as unit tests, integration tests, and functional tests. 

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**arn** | [**String**](String.md) |  |  [optional] |
|**type** | [**ReportType**](ReportType.md) |  |  [optional] |
|**name** | [**String**](String.md) |  |  [optional] |
|**reportGroupArn** | [**String**](String.md) |  |  [optional] |
|**executionId** | [**String**](String.md) |  |  [optional] |
|**status** | [**ReportStatusType**](ReportStatusType.md) |  |  [optional] |
|**created** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**expired** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**exportConfig** | [**ReportExportConfig**](ReportExportConfig.md) |  |  [optional] |
|**truncated** | [**Boolean**](Boolean.md) |  |  [optional] |
|**testSummary** | [**ReportTestSummary**](ReportTestSummary.md) |  |  [optional] |
|**codeCoverageSummary** | [**ReportCodeCoverageSummary**](ReportCodeCoverageSummary.md) |  |  [optional] |



