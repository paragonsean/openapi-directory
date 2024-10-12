# StorageManagement.StorageAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | The type of the storage account. | [optional] 
**creationTime** | **Date** | The creation date and time of the storage account in UTC. | [optional] 
**customDomain** | [**CustomDomain**](CustomDomain.md) |  | [optional] 
**lastGeoFailoverTime** | **Date** | The timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS. | [optional] 
**primaryEndpoints** | [**Endpoints**](Endpoints.md) |  | [optional] 
**primaryLocation** | **String** | The location of the primary data center for the storage account. | [optional] 
**provisioningState** | **String** | The status of the storage account at the time the operation was called. | [optional] 
**secondaryEndpoints** | [**Endpoints**](Endpoints.md) |  | [optional] 
**secondaryLocation** | **String** | The location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS. | [optional] 
**statusOfPrimary** | **String** | The status indicating whether the primary location of the storage account is available or unavailable. | [optional] 
**statusOfSecondary** | **String** | The status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS. | [optional] 



## Enum: AccountTypeEnum


* `Standard_LRS` (value: `"Standard_LRS"`)

* `Standard_ZRS` (value: `"Standard_ZRS"`)

* `Standard_GRS` (value: `"Standard_GRS"`)

* `Standard_RAGRS` (value: `"Standard_RAGRS"`)

* `Premium_LRS` (value: `"Premium_LRS"`)





## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `ResolvingDNS` (value: `"ResolvingDNS"`)

* `Succeeded` (value: `"Succeeded"`)





## Enum: StatusOfPrimaryEnum


* `Available` (value: `"Available"`)

* `Unavailable` (value: `"Unavailable"`)





## Enum: StatusOfSecondaryEnum


* `Available` (value: `"Available"`)

* `Unavailable` (value: `"Unavailable"`)




