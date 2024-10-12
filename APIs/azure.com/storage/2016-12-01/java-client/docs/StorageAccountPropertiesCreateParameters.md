

# StorageAccountPropertiesCreateParameters

The parameters used to create the storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTier** | [**AccessTierEnum**](#AccessTierEnum) | Required for storage accounts where kind &#x3D; BlobStorage. The access tier used for billing. |  [optional] |
|**customDomain** | [**CustomDomain**](CustomDomain.md) |  |  [optional] |
|**encryption** | [**Encryption**](Encryption.md) |  |  [optional] |
|**supportsHttpsTrafficOnly** | **Boolean** | Allows https traffic only to storage service if sets to true. |  [optional] |



## Enum: AccessTierEnum

| Name | Value |
|---- | -----|
| HOT | &quot;Hot&quot; |
| COOL | &quot;Cool&quot; |



