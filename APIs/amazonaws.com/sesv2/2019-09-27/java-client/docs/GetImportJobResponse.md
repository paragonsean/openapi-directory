

# GetImportJobResponse

An HTTP 200 response if the request succeeds, or an error message if the request fails.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | [**String**](String.md) |  |  [optional] |
|**importDestination** | [**GetImportJobResponseImportDestination**](GetImportJobResponseImportDestination.md) |  |  [optional] |
|**importDataSource** | [**GetImportJobResponseImportDataSource**](GetImportJobResponseImportDataSource.md) |  |  [optional] |
|**failureInfo** | [**GetImportJobResponseFailureInfo**](GetImportJobResponseFailureInfo.md) |  |  [optional] |
|**jobStatus** | [**JobStatus**](JobStatus.md) |  |  [optional] |
|**createdTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**completedTimestamp** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**processedRecordsCount** | [**Integer**](Integer.md) |  |  [optional] |
|**failedRecordsCount** | [**Integer**](Integer.md) |  |  [optional] |



