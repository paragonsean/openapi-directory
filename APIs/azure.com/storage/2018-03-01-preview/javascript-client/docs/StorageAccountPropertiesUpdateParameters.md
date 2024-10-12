# StorageManagementClient.StorageAccountPropertiesUpdateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTier** | **String** | Required for storage accounts where kind &#x3D; BlobStorage. The access tier used for billing. | [optional] 
**customDomain** | [**CustomDomain**](CustomDomain.md) |  | [optional] 
**encryption** | [**Encryption**](Encryption.md) |  | [optional] 
**networkAcls** | [**NetworkRuleSet**](NetworkRuleSet.md) |  | [optional] 
**supportsHttpsTrafficOnly** | **Boolean** | Allows https traffic only to storage service if sets to true. | [optional] [default to false]



## Enum: AccessTierEnum


* `Hot` (value: `"Hot"`)

* `Cool` (value: `"Cool"`)




