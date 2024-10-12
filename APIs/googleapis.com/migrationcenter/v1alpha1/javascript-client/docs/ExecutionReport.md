# MigrationCenterApi.ExecutionReport

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**executionErrors** | [**ValidationReport**](ValidationReport.md) |  | [optional] 
**framesReported** | **Number** | Total number of asset frames reported for the import job. | [optional] 
**jobErrors** | [**[ImportError]**](ImportError.md) | List of job-level errors. Deprecated, use the job errors under execution_errors instead. | [optional] 
**totalRowsCount** | **Number** | Total number of rows in the import job. | [optional] 


