# KeyVaultManagementClient.VaultPatchProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessPolicies** | [**[AccessPolicyEntry]**](AccessPolicyEntry.md) | An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault&#39;s tenant ID. | [optional] 
**createMode** | **String** | The vault&#39;s create mode to indicate whether the vault need to be recovered or not. | [optional] 
**enablePurgeProtection** | **Boolean** | Property specifying whether protection against purge is enabled for this vault; it is only effective if soft delete is also enabled. Once activated, the property may no longer be reset to false. | [optional] 
**enableSoftDelete** | **Boolean** | Property specifying whether recoverable deletion (&#39;soft&#39; delete) is enabled for this key vault. The property may not be set to false. | [optional] 
**enabledForDeployment** | **Boolean** | Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. | [optional] 
**enabledForDiskEncryption** | **Boolean** | Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. | [optional] 
**enabledForTemplateDeployment** | **Boolean** | Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. | [optional] 
**sku** | [**Sku**](Sku.md) |  | [optional] 
**tenantId** | **String** | The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | [optional] 



## Enum: CreateModeEnum


* `recover` (value: `"recover"`)

* `default` (value: `"default"`)




