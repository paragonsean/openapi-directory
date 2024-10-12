# DataformApi.WorkflowConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cronSchedule** | **String** | Optional. Optional schedule (in cron format) for automatic execution of this workflow config. | [optional] 
**invocationConfig** | [**InvocationConfig**](InvocationConfig.md) |  | [optional] 
**name** | **String** | Output only. The workflow config&#39;s name. | [optional] [readonly] 
**recentScheduledExecutionRecords** | [**[ScheduledExecutionRecord]**](ScheduledExecutionRecord.md) | Output only. Records of the 10 most recent scheduled execution attempts, ordered in in descending order of &#x60;execution_time&#x60;. Updated whenever automatic creation of a workflow invocation is triggered by cron_schedule. | [optional] [readonly] 
**releaseConfig** | **String** | Required. The name of the release config whose release_compilation_result should be executed. Must be in the format &#x60;projects/_*_/locations/_*_/repositories/_*_/releaseConfigs/_*&#x60;. | [optional] 
**timeZone** | **String** | Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the time zone database (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is UTC. | [optional] 


