

# StorageAccountPropertiesUpdateParameters

The parameters used when updating a storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTier** | [**AccessTierEnum**](#AccessTierEnum) | Required for storage accounts where kind &#x3D; BlobStorage. The access tier used for billing. |  [optional] |
|**azureFilesIdentityBasedAuthentication** | [**AzureFilesIdentityBasedAuthentication**](AzureFilesIdentityBasedAuthentication.md) |  |  [optional] |
|**customDomain** | [**CustomDomain**](CustomDomain.md) |  |  [optional] |
|**encryption** | [**Encryption**](Encryption.md) |  |  [optional] |
|**largeFileSharesState** | [**LargeFileSharesStateEnum**](#LargeFileSharesStateEnum) | Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled. |  [optional] |
|**networkAcls** | [**NetworkRuleSet**](NetworkRuleSet.md) |  |  [optional] |
|**routingPreference** | [**RoutingPreference**](RoutingPreference.md) |  |  [optional] |
|**supportsHttpsTrafficOnly** | **Boolean** | Allows https traffic only to storage service if sets to true. |  [optional] |



## Enum: AccessTierEnum

| Name | Value |
|---- | -----|
| HOT | &quot;Hot&quot; |
| COOL | &quot;Cool&quot; |



## Enum: LargeFileSharesStateEnum

| Name | Value |
|---- | -----|
| DISABLED | &quot;Disabled&quot; |
| ENABLED | &quot;Enabled&quot; |



