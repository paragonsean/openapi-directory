# KeyVaultManagementClient.VaultProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessPolicies** | [**[AccessPolicyEntry]**](AccessPolicyEntry.md) | An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault&#39;s tenant ID. | 
**enableSoftDelete** | **Boolean** | Property to specify whether the &#39;soft delete&#39; functionality is enabled for this key vault. | [optional] 
**enabledForDeployment** | **Boolean** | Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. | [optional] 
**enabledForDiskEncryption** | **Boolean** | Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. | [optional] 
**enabledForTemplateDeployment** | **Boolean** | Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. | [optional] 
**sku** | [**Sku**](Sku.md) |  | 
**tenantId** | **String** | The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | 
**vaultUri** | **String** | The URI of the vault for performing operations on keys and secrets. | [optional] 


