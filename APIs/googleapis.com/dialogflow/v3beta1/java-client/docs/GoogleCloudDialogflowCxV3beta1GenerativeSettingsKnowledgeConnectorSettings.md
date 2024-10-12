

# GoogleCloudDialogflowCxV3beta1GenerativeSettingsKnowledgeConnectorSettings

Settings for knowledge connector. These parameters are used for LLM prompt like \"You are . You are a helpful and verbose at , . Your task is to help humans on \".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agent** | **String** | Name of the virtual agent. Used for LLM prompt. Can be left empty. |  [optional] |
|**agentIdentity** | **String** | Identity of the agent, e.g. \&quot;virtual agent\&quot;, \&quot;AI assistant\&quot;. |  [optional] |
|**agentScope** | **String** | Agent scope, e.g. \&quot;Example company website\&quot;, \&quot;internal Example company website for employees\&quot;, \&quot;manual of car owner\&quot;. |  [optional] |
|**business** | **String** | Name of the company, organization or other entity that the agent represents. Used for knowledge connector LLM prompt and for knowledge search. |  [optional] |
|**businessDescription** | **String** | Company description, used for LLM prompt, e.g. \&quot;a family company selling freshly roasted coffee beans\&quot;. |  [optional] |
|**disableDataStoreFallback** | **Boolean** | Whether to disable fallback to Data Store search results (in case the LLM couldn&#39;t pick a proper answer). Per default the feature is enabled. |  [optional] |



