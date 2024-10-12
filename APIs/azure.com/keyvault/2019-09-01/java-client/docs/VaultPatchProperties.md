

# VaultPatchProperties

Properties of the vault

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessPolicies** | [**List&lt;AccessPolicyEntry&gt;**](AccessPolicyEntry.md) | An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault&#39;s tenant ID. |  [optional] |
|**createMode** | [**CreateModeEnum**](#CreateModeEnum) | The vault&#39;s create mode to indicate whether the vault need to be recovered or not. |  [optional] |
|**enablePurgeProtection** | **Boolean** | Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value. |  [optional] |
|**enableSoftDelete** | **Boolean** | Property to specify whether the &#39;soft delete&#39; functionality is enabled for this key vault. If omitted, assume true as default value. Once set to true, cannot be reverted to false. |  [optional] |
|**enabledForDeployment** | **Boolean** | Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault. |  [optional] |
|**enabledForDiskEncryption** | **Boolean** | Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys. |  [optional] |
|**enabledForTemplateDeployment** | **Boolean** | Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault. |  [optional] |
|**networkAcls** | [**NetworkRuleSet**](NetworkRuleSet.md) |  |  [optional] |
|**sku** | [**Sku**](Sku.md) |  |  [optional] |
|**tenantId** | **UUID** | The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault. |  [optional] |



## Enum: CreateModeEnum

| Name | Value |
|---- | -----|
| RECOVER | &quot;recover&quot; |
| DEFAULT | &quot;default&quot; |



