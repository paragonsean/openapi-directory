

# AzureCliScriptProperties

Properties of the Azure CLI script object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**azCliVersion** | **String** | Azure CLI module version to be used. |  |
|**cleanupPreference** | [**CleanupPreferenceEnum**](#CleanupPreferenceEnum) | The clean up preference when the script execution gets in a terminal state. Default setting is &#39;Always&#39;. |  [optional] |
|**outputs** | **Map&lt;String, Object&gt;** | List of script outputs. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | State of the script execution. This only appears in the response. |  [optional] [readonly] |
|**status** | [**ScriptStatus**](ScriptStatus.md) |  |  [optional] |
|**arguments** | **String** | Command line arguments to pass to the script. Arguments are separated by spaces. ex: -Name blue* -Location &#39;West US 2&#39;  |  [optional] |
|**environmentVariables** | [**List&lt;EnvironmentVariable&gt;**](EnvironmentVariable.md) | The environment variables to pass over to the script. |  [optional] |
|**forceUpdateTag** | **String** | Gets or sets how the deployment script should be forced to execute even if the script resource has not changed. Can be current time stamp or a GUID. |  [optional] |
|**primaryScriptUri** | **String** | Uri for the script. This is the entry point for the external script. |  [optional] |
|**retentionInterval** | **String** | Interval for which the service retains the script resource after it reaches a terminal state. Resource will be deleted when this duration expires. Duration is based on ISO 8601 pattern (for example P7D means one week). |  |
|**scriptContent** | **String** | Script body. |  [optional] |
|**supportingScriptUris** | **List&lt;String&gt;** | Supporting files for the external script. |  [optional] |
|**timeout** | **String** | Maximum allowed script execution time specified in ISO 8601 format. Default value is PT1H |  [optional] |



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



