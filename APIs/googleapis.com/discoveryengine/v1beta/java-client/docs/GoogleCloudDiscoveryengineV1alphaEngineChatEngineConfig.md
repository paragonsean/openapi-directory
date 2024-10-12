

# GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfig

Configurations for a Chat Engine.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentCreationConfig** | [**GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigAgentCreationConfig**](GoogleCloudDiscoveryengineV1alphaEngineChatEngineConfigAgentCreationConfig.md) |  |  [optional] |
|**dialogflowAgentToLink** | **String** | The resource name of an exist Dialogflow agent to link to this Chat Engine. Customers can either provide &#x60;agent_creation_config&#x60; to create agent or provide an agent name that links the agent with the Chat engine. Format: &#x60;projects//locations//agents/&#x60;. Note that the &#x60;dialogflow_agent_to_link&#x60; are one-time consumed by and passed to Dialogflow service. It means they cannot be retrieved using EngineService.GetEngine or EngineService.ListEngines API after engine creation. Please use ChatEngineMetadata.dialogflow_agent for actual agent association after Engine is created. |  [optional] |



