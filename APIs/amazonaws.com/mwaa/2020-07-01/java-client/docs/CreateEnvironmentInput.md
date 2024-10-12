

# CreateEnvironmentInput

This section contains the Amazon Managed Workflows for Apache Airflow (MWAA) API reference documentation to create an environment. For more information, see <a href=\"https://docs.aws.amazon.com/mwaa/latest/userguide/get-started.html\">Get started with Amazon Managed Workflows for Apache Airflow</a>.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**airflowConfigurationOptions** | [**Map**](Map.md) |  |  [optional] |
|**airflowVersion** | [**String**](String.md) |  |  [optional] |
|**dagS3Path** | [**String**](String.md) |  |  |
|**environmentClass** | [**String**](String.md) |  |  [optional] |
|**executionRoleArn** | [**String**](String.md) |  |  |
|**kmsKey** | [**String**](String.md) |  |  [optional] |
|**loggingConfiguration** | [**CreateEnvironmentInputLoggingConfiguration**](CreateEnvironmentInputLoggingConfiguration.md) |  |  [optional] |
|**maxWorkers** | [**Integer**](Integer.md) |  |  [optional] |
|**minWorkers** | [**Integer**](Integer.md) |  |  [optional] |
|**networkConfiguration** | [**CreateEnvironmentInputNetworkConfiguration**](CreateEnvironmentInputNetworkConfiguration.md) |  |  |
|**pluginsS3ObjectVersion** | [**String**](String.md) |  |  [optional] |
|**pluginsS3Path** | [**String**](String.md) |  |  [optional] |
|**requirementsS3ObjectVersion** | [**String**](String.md) |  |  [optional] |
|**requirementsS3Path** | [**String**](String.md) |  |  [optional] |
|**schedulers** | [**Integer**](Integer.md) |  |  [optional] |
|**sourceBucketArn** | [**String**](String.md) |  |  |
|**startupScriptS3ObjectVersion** | [**String**](String.md) |  |  [optional] |
|**startupScriptS3Path** | [**String**](String.md) |  |  [optional] |
|**tags** | [**Map**](Map.md) |  |  [optional] |
|**webserverAccessMode** | [**WebserverAccessMode**](WebserverAccessMode.md) |  |  [optional] |
|**weeklyMaintenanceWindowStart** | [**String**](String.md) |  |  [optional] |



