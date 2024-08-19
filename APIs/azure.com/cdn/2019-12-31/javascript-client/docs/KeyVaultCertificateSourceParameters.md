# CdnManagementClient.KeyVaultCertificateSourceParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**odataType** | **String** |  | 
**deleteRule** | **String** | Describes the action that shall be taken when the certificate is removed from Key Vault. | 
**resourceGroupName** | **String** | Resource group of the user&#39;s Key Vault containing the SSL certificate | 
**secretName** | **String** | The name of Key Vault Secret (representing the full certificate PFX) in Key Vault. | 
**secretVersion** | **String** | The version(GUID) of Key Vault Secret in Key Vault. | 
**subscriptionId** | **String** | Subscription Id of the user&#39;s Key Vault containing the SSL certificate | 
**updateRule** | **String** | Describes the action that shall be taken when the certificate is updated in Key Vault. | 
**vaultName** | **String** | The name of the user&#39;s Key Vault containing the SSL certificate | 



## Enum: OdataTypeEnum


* `#Microsoft.Azure.Cdn.Models.KeyVaultCertificateSourceParameters` (value: `"#Microsoft.Azure.Cdn.Models.KeyVaultCertificateSourceParameters"`)





## Enum: DeleteRuleEnum


* `NoAction` (value: `"NoAction"`)





## Enum: UpdateRuleEnum


* `NoAction` (value: `"NoAction"`)




