

# ExportJobProperties

The properties of a FHIR export job, including the ID, ARN, name, and the status of the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | [**String**](String.md) |  |  |
|**jobName** | [**String**](String.md) |  |  [optional] |
|**jobStatus** | [**JobStatus**](JobStatus.md) |  |  |
|**submitTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**datastoreId** | [**String**](String.md) |  |  |
|**outputDataConfig** | [**StartFHIRExportJobRequestOutputDataConfig**](StartFHIRExportJobRequestOutputDataConfig.md) |  |  |
|**dataAccessRoleArn** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |



