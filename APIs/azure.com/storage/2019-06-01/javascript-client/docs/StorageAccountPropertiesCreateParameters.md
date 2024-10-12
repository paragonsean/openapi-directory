# StorageManagementClient.StorageAccountPropertiesCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTier** | **String** | Required for storage accounts where kind &#x3D; BlobStorage. The access tier used for billing. | [optional] 
**azureFilesIdentityBasedAuthentication** | [**AzureFilesIdentityBasedAuthentication**](AzureFilesIdentityBasedAuthentication.md) |  | [optional] 
**customDomain** | [**CustomDomain**](CustomDomain.md) |  | [optional] 
**encryption** | [**Encryption**](Encryption.md) |  | [optional] 
**isHnsEnabled** | **Boolean** | Account HierarchicalNamespace enabled if sets to true. | [optional] 
**largeFileSharesState** | **String** | Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled. | [optional] 
**networkAcls** | [**NetworkRuleSet**](NetworkRuleSet.md) |  | [optional] 
**routingPreference** | [**RoutingPreference**](RoutingPreference.md) |  | [optional] 
**supportsHttpsTrafficOnly** | **Boolean** | Allows https traffic only to storage service if sets to true. The default value is true since API version 2019-04-01. | [optional] 



## Enum: AccessTierEnum


* `Hot` (value: `"Hot"`)

* `Cool` (value: `"Cool"`)





## Enum: LargeFileSharesStateEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




