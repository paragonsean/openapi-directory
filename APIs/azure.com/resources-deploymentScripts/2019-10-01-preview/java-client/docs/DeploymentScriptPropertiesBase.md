

# DeploymentScriptPropertiesBase

Common properties for the deployment script.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cleanupPreference** | [**CleanupPreferenceEnum**](#CleanupPreferenceEnum) | The clean up preference when the script execution gets in a terminal state. Default setting is &#39;Always&#39;. |  [optional] |
|**outputs** | **Map&lt;String, Object&gt;** | List of script outputs. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | State of the script execution. This only appears in the response. |  [optional] [readonly] |
|**status** | [**ScriptStatus**](ScriptStatus.md) |  |  [optional] |



## Enum: CleanupPreferenceEnum

| Name | Value |
|---- | -----|
| ALWAYS | &quot;Always&quot; |
| ON_SUCCESS | &quot;OnSuccess&quot; |
| ON_EXPIRATION | &quot;OnExpiration&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| PROVISIONING_RESOURCES | &quot;ProvisioningResources&quot; |
| RUNNING | &quot;Running&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |
| FAILED | &quot;Failed&quot; |
| CANCELED | &quot;Canceled&quot; |



