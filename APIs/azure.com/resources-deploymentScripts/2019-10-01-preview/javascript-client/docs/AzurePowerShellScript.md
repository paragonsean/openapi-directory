# DeploymentScriptsClient.AzurePowerShellScript

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**AzurePowerShellScriptProperties**](AzurePowerShellScriptProperties.md) |  | 
**identity** | [**ManagedServiceIdentity**](ManagedServiceIdentity.md) |  | 
**kind** | **String** | Type of the script. | 
**location** | **String** | The location of the ACI and the storage account for the deployment script. | 
**tags** | **{String: String}** | Resource tags. | [optional] 
**id** | **String** | String Id used to locate any resource on Azure. | [optional] [readonly] 
**name** | **String** | Name of this resource. | [optional] [readonly] 
**type** | **String** | Type of this resource. | [optional] [readonly] 



## Enum: KindEnum


* `AzurePowerShell` (value: `"AzurePowerShell"`)

* `AzureCLI` (value: `"AzureCLI"`)




