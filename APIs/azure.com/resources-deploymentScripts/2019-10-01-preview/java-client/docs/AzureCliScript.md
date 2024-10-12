

# AzureCliScript

Object model for the Azure CLI script.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**properties** | [**AzureCliScriptProperties**](AzureCliScriptProperties.md) |  |  |
|**identity** | [**ManagedServiceIdentity**](ManagedServiceIdentity.md) |  |  |
|**kind** | [**KindEnum**](#KindEnum) | Type of the script. |  |
|**location** | **String** | The location of the ACI and the storage account for the deployment script. |  |
|**tags** | **Map&lt;String, String&gt;** | Resource tags. |  [optional] |
|**id** | **String** | String Id used to locate any resource on Azure. |  [optional] [readonly] |
|**name** | **String** | Name of this resource. |  [optional] [readonly] |
|**type** | **String** | Type of this resource. |  [optional] [readonly] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| AZURE_POWER_SHELL | &quot;AzurePowerShell&quot; |
| AZURE_CLI | &quot;AzureCLI&quot; |



