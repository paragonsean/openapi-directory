

# BuildSystemSharedDTOAgent

A DTO for an IAgent

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentID** | **Integer** | The id of the Agent |  [optional] |
|**keepAliveInterval** | **Integer** | The &#39;Heartbeat Interval&#39; used by the Build Agent. |  |
|**machineName** | **String** | The machine name of the computer the agent is running on |  |
|**status** | [**BuildSystemSharedDTOAgentStatus**](BuildSystemSharedDTOAgentStatus.md) |  |  |
|**stepConfigurations** | [**List&lt;BuildSystemSharedDTOStepConfiguration&gt;**](BuildSystemSharedDTOStepConfiguration.md) | The agent&#39;s step configurations |  [optional] [readonly] |
|**userID** | **Integer** | The UserID of the Agent |  |



