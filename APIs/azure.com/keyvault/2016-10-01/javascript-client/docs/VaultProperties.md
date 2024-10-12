# KeyVaultManagementClient.VaultProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessPolicies** | [**[AccessPolicyEntry]**](AccessPolicyEntry.md) | An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault&#39;s tenant ID. When &#x60;createMode&#x60; is set to &#x60;recover&#x60;, access policies are not required. Otherwise, access policies are required. | [optional] 
**createMode** | **String** | The vault&#39;s create mode to indicate whether the vault need to be recovered or not. | [optional] 
**enablePurgeProtection** | **Boolean** | Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value. | [optional] 
**enableSoftDelete** | **Boolean** | Property specifying whether recoverable deletion is enabled for this key vault. Setting this property to true activates the soft delete feature, whereby vaults or vault entities can be recovered after deletion. Enabling this functionality is irreversible - that is, the property does not accept false as its value. | [optional] 
**enabledForDeployment** | **Boolean** | Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. | [optional] 
**enabledForDiskEncryption** | **Boolean** | Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. | [optional] 
**enabledForTemplateDeployment** | **Boolean** | Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. | [optional] 
**sku** | [**Sku**](Sku.md) |  | 
**tenantId** | **String** | The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. | 
**vaultUri** | **String** | The URI of the vault for performing operations on keys and secrets. | [optional] 



## Enum: CreateModeEnum


* `recover` (value: `"recover"`)

* `default` (value: `"default"`)




