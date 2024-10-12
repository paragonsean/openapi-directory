# EmrServerless.StartJobRunRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clientToken** | **String** | The client idempotency token of the job run to start. Its value must be unique for each request. | 
**executionRoleArn** | **String** | The execution role ARN for the job run. | 
**jobDriver** | [**StartJobRunRequestJobDriver**](StartJobRunRequestJobDriver.md) |  | [optional] 
**configurationOverrides** | [**StartJobRunRequestConfigurationOverrides**](StartJobRunRequestConfigurationOverrides.md) |  | [optional] 
**tags** | **{String: String}** | The tags assigned to the job run. | [optional] 
**executionTimeoutMinutes** | **Number** | The maximum duration for the job run to run. If the job run runs beyond this duration, it will be automatically cancelled. | [optional] 
**name** | **String** | The optional job run name. This doesn&#39;t have to be unique. | [optional] 


