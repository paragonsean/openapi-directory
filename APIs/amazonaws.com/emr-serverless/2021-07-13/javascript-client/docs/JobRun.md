# EmrServerless.JobRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationId** | **String** |  | 
**jobRunId** | **String** |  | 
**name** | **String** |  | [optional] 
**arn** | **String** |  | 
**createdBy** | **String** |  | 
**createdAt** | **Date** |  | 
**updatedAt** | **Date** |  | 
**executionRole** | **String** |  | 
**state** | [**JobRunState**](JobRunState.md) |  | 
**stateDetails** | **String** |  | 
**releaseLabel** | **String** |  | 
**configurationOverrides** | [**JobRunConfigurationOverrides**](JobRunConfigurationOverrides.md) |  | [optional] 
**jobDriver** | [**JobRunJobDriver**](JobRunJobDriver.md) |  | 
**tags** | **Object** |  | [optional] 
**totalResourceUtilization** | [**JobRunTotalResourceUtilization**](JobRunTotalResourceUtilization.md) |  | [optional] 
**networkConfiguration** | [**NetworkConfiguration**](NetworkConfiguration.md) |  | [optional] 
**totalExecutionDurationSeconds** | **Number** |  | [optional] 
**executionTimeoutMinutes** | **Number** |  | [optional] 
**billedResourceUtilization** | [**JobRunBilledResourceUtilization**](JobRunBilledResourceUtilization.md) |  | [optional] 


