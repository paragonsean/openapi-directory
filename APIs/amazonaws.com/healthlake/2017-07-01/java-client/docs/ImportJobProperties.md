

# ImportJobProperties

Displays the properties of the import job, including the ID, Arn, Name, and the status of the data store.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**jobId** | [**String**](String.md) |  |  |
|**jobName** | [**String**](String.md) |  |  [optional] |
|**jobStatus** | [**JobStatus**](JobStatus.md) |  |  |
|**submitTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**endTime** | [**OffsetDateTime**](OffsetDateTime.md) |  |  [optional] |
|**datastoreId** | [**String**](String.md) |  |  |
|**inputDataConfig** | [**ImportJobPropertiesInputDataConfig**](ImportJobPropertiesInputDataConfig.md) |  |  |
|**jobOutputDataConfig** | [**OutputDataConfig**](OutputDataConfig.md) |  |  [optional] |
|**dataAccessRoleArn** | [**String**](String.md) |  |  [optional] |
|**message** | [**String**](String.md) |  |  [optional] |



