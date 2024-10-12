

# OrchestratorVersionProfile

The profile of an orchestrator and its available versions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**_default** | **Boolean** | Installed by default if version is not specified. |  [optional] |
|**isPreview** | **Boolean** | Whether Kubernetes version is currently in preview. |  [optional] |
|**orchestratorType** | **String** | Orchestrator type. |  |
|**orchestratorVersion** | **String** | Orchestrator version (major, minor, patch). |  |
|**upgrades** | [**List&lt;OrchestratorProfile&gt;**](OrchestratorProfile.md) | The list of available upgrade versions. |  [optional] |



