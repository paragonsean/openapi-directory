# AmazonMwaa.CreateEnvironmentInput

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**airflowConfigurationOptions** | **Object** |  | [optional] 
**airflowVersion** | **String** |  | [optional] 
**dagS3Path** | **String** |  | 
**environmentClass** | **String** |  | [optional] 
**executionRoleArn** | **String** |  | 
**kmsKey** | **String** |  | [optional] 
**loggingConfiguration** | [**CreateEnvironmentInputLoggingConfiguration**](CreateEnvironmentInputLoggingConfiguration.md) |  | [optional] 
**maxWorkers** | **Number** |  | [optional] 
**minWorkers** | **Number** |  | [optional] 
**networkConfiguration** | [**CreateEnvironmentInputNetworkConfiguration**](CreateEnvironmentInputNetworkConfiguration.md) |  | 
**pluginsS3ObjectVersion** | **String** |  | [optional] 
**pluginsS3Path** | **String** |  | [optional] 
**requirementsS3ObjectVersion** | **String** |  | [optional] 
**requirementsS3Path** | **String** |  | [optional] 
**schedulers** | **Number** |  | [optional] 
**sourceBucketArn** | **String** |  | 
**startupScriptS3ObjectVersion** | **String** |  | [optional] 
**startupScriptS3Path** | **String** |  | [optional] 
**tags** | **Object** |  | [optional] 
**webserverAccessMode** | [**WebserverAccessMode**](WebserverAccessMode.md) |  | [optional] 
**weeklyMaintenanceWindowStart** | **String** |  | [optional] 


