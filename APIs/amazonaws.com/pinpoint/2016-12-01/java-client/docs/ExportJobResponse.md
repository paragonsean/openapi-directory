

# ExportJobResponse

Provides information about the status and settings of a job that exports endpoint definitions to a file. The file can be added directly to an Amazon Simple Storage Service (Amazon S3) bucket by using the Amazon Pinpoint API or downloaded directly to a computer by using the Amazon Pinpoint console.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationId** | [**String**](String.md) |  |  |
|**completedPieces** | [**Integer**](Integer.md) |  |  [optional] |
|**completionDate** | [**String**](String.md) |  |  [optional] |
|**creationDate** | [**String**](String.md) |  |  |
|**definition** | [**ExportJobResponseDefinition**](ExportJobResponseDefinition.md) |  |  |
|**failedPieces** | [**Integer**](Integer.md) |  |  [optional] |
|**failures** | [**List**](List.md) |  |  [optional] |
|**id** | [**String**](String.md) |  |  |
|**jobStatus** | [**JobStatus**](JobStatus.md) |  |  |
|**totalFailures** | [**Integer**](Integer.md) |  |  [optional] |
|**totalPieces** | [**Integer**](Integer.md) |  |  [optional] |
|**totalProcessed** | [**Integer**](Integer.md) |  |  [optional] |
|**type** | [**String**](String.md) |  |  |



