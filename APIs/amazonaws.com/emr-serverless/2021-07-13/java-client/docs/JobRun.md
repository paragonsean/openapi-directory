

# JobRun

Information about a job run. A job run is a unit of work, such as a Spark JAR, Hive query, or SparkSQL query, that you submit to an Amazon EMR Serverless application.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationId** | [**String**](String.md) |  |  |
|**jobRunId** | [**String**](String.md) |  |  |
|**name** | [**String**](String.md) |  |  [optional] |
|**arn** | [**String**](String.md) |  |  |
|**createdBy** | [**String**](String.md) |  |  |
|**createdAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**updatedAt** | [**OffsetDateTime**](OffsetDateTime.md) |  |  |
|**executionRole** | [**String**](String.md) |  |  |
|**state** | [**JobRunState**](JobRunState.md) |  |  |
|**stateDetails** | [**String**](String.md) |  |  |
|**releaseLabel** | [**String**](String.md) |  |  |
|**configurationOverrides** | [**JobRunConfigurationOverrides**](JobRunConfigurationOverrides.md) |  |  [optional] |
|**jobDriver** | [**JobRunJobDriver**](JobRunJobDriver.md) |  |  |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**totalResourceUtilization** | [**JobRunTotalResourceUtilization**](JobRunTotalResourceUtilization.md) |  |  [optional] |
|**networkConfiguration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  |  [optional] |
|**totalExecutionDurationSeconds** | [**Integer**](Integer.md) |  |  [optional] |
|**executionTimeoutMinutes** | [**Integer**](Integer.md) |  |  [optional] |
|**billedResourceUtilization** | [**JobRunBilledResourceUtilization**](JobRunBilledResourceUtilization.md) |  |  [optional] |



