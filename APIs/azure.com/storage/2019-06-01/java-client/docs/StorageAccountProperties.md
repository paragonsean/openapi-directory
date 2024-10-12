

# StorageAccountProperties

Properties of the storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accessTier** | [**AccessTierEnum**](#AccessTierEnum) | Required for storage accounts where kind &#x3D; BlobStorage. The access tier used for billing. |  [optional] [readonly] |
|**azureFilesIdentityBasedAuthentication** | [**AzureFilesIdentityBasedAuthentication**](AzureFilesIdentityBasedAuthentication.md) |  |  [optional] |
|**blobRestoreStatus** | [**BlobRestoreStatus**](BlobRestoreStatus.md) |  |  [optional] |
|**creationTime** | **OffsetDateTime** | Gets the creation date and time of the storage account in UTC. |  [optional] [readonly] |
|**customDomain** | [**CustomDomain**](CustomDomain.md) |  |  [optional] |
|**encryption** | [**Encryption**](Encryption.md) |  |  [optional] |
|**failoverInProgress** | **Boolean** | If the failover is in progress, the value will be true, otherwise, it will be null. |  [optional] [readonly] |
|**geoReplicationStats** | [**GeoReplicationStats**](GeoReplicationStats.md) |  |  [optional] |
|**isHnsEnabled** | **Boolean** | Account HierarchicalNamespace enabled if sets to true. |  [optional] |
|**largeFileSharesState** | [**LargeFileSharesStateEnum**](#LargeFileSharesStateEnum) | Allow large file shares if sets to Enabled. It cannot be disabled once it is enabled. |  [optional] |
|**lastGeoFailoverTime** | **OffsetDateTime** | Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS. |  [optional] [readonly] |
|**networkAcls** | [**NetworkRuleSet**](NetworkRuleSet.md) |  |  [optional] |
|**primaryEndpoints** | [**Endpoints**](Endpoints.md) |  |  [optional] |
|**primaryLocation** | **String** | Gets the location of the primary data center for the storage account. |  [optional] [readonly] |
|**privateEndpointConnections** | [**List&lt;PrivateEndpointConnection&gt;**](PrivateEndpointConnection.md) | List of private endpoint connection associated with the specified storage account |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Gets the status of the storage account at the time the operation was called. |  [optional] [readonly] |
|**routingPreference** | [**RoutingPreference**](RoutingPreference.md) |  |  [optional] |
|**secondaryEndpoints** | [**Endpoints**](Endpoints.md) |  |  [optional] |
|**secondaryLocation** | **String** | Gets the location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS. |  [optional] [readonly] |
|**statusOfPrimary** | [**StatusOfPrimaryEnum**](#StatusOfPrimaryEnum) | Gets the status indicating whether the primary location of the storage account is available or unavailable. |  [optional] [readonly] |
|**statusOfSecondary** | [**StatusOfSecondaryEnum**](#StatusOfSecondaryEnum) | Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS. |  [optional] [readonly] |
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



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| RESOLVING_DNS | &quot;ResolvingDNS&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



## Enum: StatusOfPrimaryEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



## Enum: StatusOfSecondaryEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;available&quot; |
| UNAVAILABLE | &quot;unavailable&quot; |



