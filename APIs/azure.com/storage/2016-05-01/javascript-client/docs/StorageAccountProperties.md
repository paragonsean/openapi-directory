# StorageManagement.StorageAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessTier** | **String** | Required for storage accounts where kind &#x3D; BlobStorage. The access tier used for billing. | [optional] [readonly] 
**creationTime** | **Date** | Gets the creation date and time of the storage account in UTC. | [optional] [readonly] 
**customDomain** | [**CustomDomain**](CustomDomain.md) |  | [optional] 
**encryption** | [**Encryption**](Encryption.md) |  | [optional] 
**lastGeoFailoverTime** | **Date** | Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS. | [optional] [readonly] 
**primaryEndpoints** | [**Endpoints**](Endpoints.md) |  | [optional] 
**primaryLocation** | **String** | Gets the location of the primary data center for the storage account. | [optional] [readonly] 
**provisioningState** | **String** | Gets the status of the storage account at the time the operation was called. | [optional] [readonly] 
**secondaryEndpoints** | [**Endpoints**](Endpoints.md) |  | [optional] 
**secondaryLocation** | **String** | Gets the location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS. | [optional] [readonly] 
**statusOfPrimary** | **String** | Gets the status indicating whether the primary location of the storage account is available or unavailable. | [optional] [readonly] 
**statusOfSecondary** | **String** | Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS. | [optional] [readonly] 



## Enum: AccessTierEnum


* `Hot` (value: `"Hot"`)

* `Cool` (value: `"Cool"`)





## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `ResolvingDNS` (value: `"ResolvingDNS"`)

* `Succeeded` (value: `"Succeeded"`)





## Enum: StatusOfPrimaryEnum


* `available` (value: `"available"`)

* `unavailable` (value: `"unavailable"`)





## Enum: StatusOfSecondaryEnum


* `available` (value: `"available"`)

* `unavailable` (value: `"unavailable"`)




