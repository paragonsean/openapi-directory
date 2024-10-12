# BatchApi.AgentInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobId** | **String** | Optional. The assigned Job ID | [optional] 
**reportTime** | **String** | When the AgentInfo is generated. | [optional] 
**state** | **String** | Agent state. | [optional] 
**taskGroupId** | **String** | The assigned task group ID. | [optional] 
**tasks** | [**[AgentTaskInfo]**](AgentTaskInfo.md) | Task Info. | [optional] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"AGENT_STATE_UNSPECIFIED"`)

* `STARTING` (value: `"AGENT_STARTING"`)

* `RUNNING` (value: `"AGENT_RUNNING"`)

* `STOPPED` (value: `"AGENT_STOPPED"`)




