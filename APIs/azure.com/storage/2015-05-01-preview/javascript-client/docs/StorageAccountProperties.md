# StorageManagementClient.StorageAccountProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountType** | **String** | Gets the type of the storage account. | [optional] 
**creationTime** | **Date** | Gets the creation date and time of the storage account in UTC. | [optional] 
**customDomain** | [**CustomDomain**](CustomDomain.md) |  | [optional] 
**lastGeoFailoverTime** | **Date** | Gets the timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is StandardGRS or StandardRAGRS. | [optional] 
**primaryEndpoints** | [**Endpoints**](Endpoints.md) |  | [optional] 
**primaryLocation** | **String** | Gets the location of the primary for the storage account. | [optional] 
**provisioningState** | **String** | Gets the status of the storage account at the time the operation was called. | [optional] 
**secondaryEndpoints** | [**Endpoints**](Endpoints.md) |  | [optional] 
**secondaryLocation** | **String** | Gets the location of the geo replicated secondary for the storage account. Only available if the accountType is StandardGRS or StandardRAGRS. | [optional] 
**statusOfPrimary** | **String** | Gets the status indicating whether the primary location of the storage account is available or unavailable. | [optional] 
**statusOfSecondary** | **String** | Gets the status indicating whether the secondary location of the storage account is available or unavailable. Only available if the accountType is StandardGRS or StandardRAGRS. | [optional] 



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




