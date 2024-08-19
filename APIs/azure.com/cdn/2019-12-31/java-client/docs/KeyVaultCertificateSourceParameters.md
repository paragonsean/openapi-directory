

# KeyVaultCertificateSourceParameters

Describes the parameters for using a user's KeyVault certificate for securing custom domain.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atOdataType** | [**AtOdataTypeEnum**](#AtOdataTypeEnum) |  |  |
|**deleteRule** | [**DeleteRuleEnum**](#DeleteRuleEnum) | Describes the action that shall be taken when the certificate is removed from Key Vault. |  |
|**resourceGroupName** | **String** | Resource group of the user&#39;s Key Vault containing the SSL certificate |  |
|**secretName** | **String** | The name of Key Vault Secret (representing the full certificate PFX) in Key Vault. |  |
|**secretVersion** | **String** | The version(GUID) of Key Vault Secret in Key Vault. |  |
|**subscriptionId** | **String** | Subscription Id of the user&#39;s Key Vault containing the SSL certificate |  |
|**updateRule** | [**UpdateRuleEnum**](#UpdateRuleEnum) | Describes the action that shall be taken when the certificate is updated in Key Vault. |  |
|**vaultName** | **String** | The name of the user&#39;s Key Vault containing the SSL certificate |  |



## Enum: AtOdataTypeEnum

| Name | Value |
|---- | -----|
| _MICROSOFT_AZURE_CDN_MODELS_KEY_VAULT_CERTIFICATE_SOURCE_PARAMETERS | &quot;#Microsoft.Azure.Cdn.Models.KeyVaultCertificateSourceParameters&quot; |



## Enum: DeleteRuleEnum

| Name | Value |
|---- | -----|
| NO_ACTION | &quot;NoAction&quot; |



## Enum: UpdateRuleEnum

| Name | Value |
|---- | -----|
| NO_ACTION | &quot;NoAction&quot; |



