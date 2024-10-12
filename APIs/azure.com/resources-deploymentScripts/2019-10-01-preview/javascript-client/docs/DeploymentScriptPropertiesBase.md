# DeploymentScriptsClient.DeploymentScriptPropertiesBase

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cleanupPreference** | **String** | The clean up preference when the script execution gets in a terminal state. Default setting is &#39;Always&#39;. | [optional] 
**outputs** | **{String: Object}** | List of script outputs. | [optional] [readonly] 
**provisioningState** | **String** | State of the script execution. This only appears in the response. | [optional] [readonly] 
**status** | [**ScriptStatus**](ScriptStatus.md) |  | [optional] 



## Enum: CleanupPreferenceEnum


* `Always` (value: `"Always"`)

* `OnSuccess` (value: `"OnSuccess"`)

* `OnExpiration` (value: `"OnExpiration"`)





## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `ProvisioningResources` (value: `"ProvisioningResources"`)

* `Running` (value: `"Running"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




