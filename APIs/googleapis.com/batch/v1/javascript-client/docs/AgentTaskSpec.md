# BatchApi.AgentTaskSpec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | [**AgentEnvironment**](AgentEnvironment.md) |  | [optional] 
**maxRunDuration** | **String** | Maximum duration the task should run. The task will be killed and marked as FAILED if over this limit. | [optional] 
**runnables** | [**[AgentTaskRunnable]**](AgentTaskRunnable.md) | AgentTaskRunnable is runanbles that will be executed on the agent. | [optional] 
**userAccount** | [**AgentTaskUserAccount**](AgentTaskUserAccount.md) |  | [optional] 


