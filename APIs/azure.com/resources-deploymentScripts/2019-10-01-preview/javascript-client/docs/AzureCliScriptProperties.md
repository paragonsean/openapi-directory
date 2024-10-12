# DeploymentScriptsClient.AzureCliScriptProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**azCliVersion** | **String** | Azure CLI module version to be used. | 
**cleanupPreference** | **String** | The clean up preference when the script execution gets in a terminal state. Default setting is &#39;Always&#39;. | [optional] 
**outputs** | **{String: Object}** | List of script outputs. | [optional] [readonly] 
**provisioningState** | **String** | State of the script execution. This only appears in the response. | [optional] [readonly] 
**status** | [**ScriptStatus**](ScriptStatus.md) |  | [optional] 
**_arguments** | **String** | Command line arguments to pass to the script. Arguments are separated by spaces. ex: -Name blue* -Location &#39;West US 2&#39;  | [optional] 
**environmentVariables** | [**[EnvironmentVariable]**](EnvironmentVariable.md) | The environment variables to pass over to the script. | [optional] 
**forceUpdateTag** | **String** | Gets or sets how the deployment script should be forced to execute even if the script resource has not changed. Can be current time stamp or a GUID. | [optional] 
**primaryScriptUri** | **String** | Uri for the script. This is the entry point for the external script. | [optional] 
**retentionInterval** | **String** | Interval for which the service retains the script resource after it reaches a terminal state. Resource will be deleted when this duration expires. Duration is based on ISO 8601 pattern (for example P7D means one week). | 
**scriptContent** | **String** | Script body. | [optional] 
**supportingScriptUris** | **[String]** | Supporting files for the external script. | [optional] 
**timeout** | **String** | Maximum allowed script execution time specified in ISO 8601 format. Default value is PT1H | [optional] 



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




