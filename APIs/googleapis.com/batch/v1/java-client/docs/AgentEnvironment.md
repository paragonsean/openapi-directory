

# AgentEnvironment

AgentEnvironment is the Environment representation between Agent and CLH communication. The environment is used in both task level and agent level.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**encryptedVariables** | [**AgentKMSEnvMap**](AgentKMSEnvMap.md) |  |  [optional] |
|**secretVariables** | **Map&lt;String, String&gt;** | A map of environment variable names to Secret Manager secret names. The VM will access the named secrets to set the value of each environment variable. |  [optional] |
|**variables** | **Map&lt;String, String&gt;** | A map of environment variable names to values. |  [optional] |



