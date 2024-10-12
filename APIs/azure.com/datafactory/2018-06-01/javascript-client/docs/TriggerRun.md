# DataFactoryManagementClient.TriggerRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dependencyStatus** | **{String: Object}** | Status of the upstream pipelines. | [optional] [readonly] 
**message** | **String** | Trigger error message. | [optional] [readonly] 
**properties** | **{String: String}** | List of property name and value related to trigger run. Name, value pair depends on type of trigger. | [optional] [readonly] 
**runDimension** | **{String: String}** | Run dimension for which trigger was fired. | [optional] [readonly] 
**status** | **String** | Trigger run status. | [optional] [readonly] 
**triggerName** | **String** | Trigger name. | [optional] [readonly] 
**triggerRunId** | **String** | Trigger run id. | [optional] [readonly] 
**triggerRunTimestamp** | **Date** | Trigger run start time. | [optional] [readonly] 
**triggerType** | **String** | Trigger type. | [optional] [readonly] 
**triggeredPipelines** | **{String: String}** | List of pipeline name and run Id triggered by the trigger run. | [optional] [readonly] 



## Enum: StatusEnum


* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Inprogress` (value: `"Inprogress"`)




