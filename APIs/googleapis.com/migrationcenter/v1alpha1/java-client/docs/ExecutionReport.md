

# ExecutionReport

A resource that reports result of the import job execution.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**executionErrors** | [**ValidationReport**](ValidationReport.md) |  |  [optional] |
|**framesReported** | **Integer** | Total number of asset frames reported for the import job. |  [optional] |
|**jobErrors** | [**List&lt;ImportError&gt;**](ImportError.md) | List of job-level errors. Deprecated, use the job errors under execution_errors instead. |  [optional] |
|**totalRowsCount** | **Integer** | Total number of rows in the import job. |  [optional] |



