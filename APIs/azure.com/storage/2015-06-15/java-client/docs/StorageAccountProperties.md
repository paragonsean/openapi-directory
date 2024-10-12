

# StorageAccountProperties

Properties of the storage account.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountType** | [**AccountTypeEnum**](#AccountTypeEnum) | The type of the storage account. |  [optional] |
|**creationTime** | **OffsetDateTime** | The creation date and time of the storage account in UTC. |  [optional] |
|**customDomain** | [**CustomDomain**](CustomDomain.md) |  |  [optional] |
|**lastGeoFailoverTime** | **OffsetDateTime** | The timestamp of the most recent instance of a failover to the secondary location. Only the most recent timestamp is retained. This element is not returned if there has never been a failover instance. Only available if the accountType is Standard_GRS or Standard_RAGRS. |  [optional] |
|**primaryEndpoints** | [**Endpoints**](Endpoints.md) |  |  [optional] |
|**primaryLocation** | **String** | The location of the primary data center for the storage account. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The status of the storage account at the time the operation was called. |  [optional] |
|**secondaryEndpoints** | [**Endpoints**](Endpoints.md) |  |  [optional] |
|**secondaryLocation** | **String** | The location of the geo-replicated secondary for the storage account. Only available if the accountType is Standard_GRS or Standard_RAGRS. |  [optional] |
|**statusOfPrimary** | [**StatusOfPrimaryEnum**](#StatusOfPrimaryEnum) | The status indicating whether the primary location of the storage account is available or unavailable. |  [optional] |
|**statusOfSecondary** | [**StatusOfSecondaryEnum**](#StatusOfSecondaryEnum) | The status indicating whether the secondary location of the storage account is available or unavailable. Only available if the SKU name is Standard_GRS or Standard_RAGRS. |  [optional] |



## Enum: AccountTypeEnum

| Name | Value |
|---- | -----|
| STANDARD_LRS | &quot;Standard_LRS&quot; |
| STANDARD_ZRS | &quot;Standard_ZRS&quot; |
| STANDARD_GRS | &quot;Standard_GRS&quot; |
| STANDARD_RAGRS | &quot;Standard_RAGRS&quot; |
| PREMIUM_LRS | &quot;Premium_LRS&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| CREATING | &quot;Creating&quot; |
| RESOLVING_DNS | &quot;ResolvingDNS&quot; |
| SUCCEEDED | &quot;Succeeded&quot; |



## Enum: StatusOfPrimaryEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;Available&quot; |
| UNAVAILABLE | &quot;Unavailable&quot; |



## Enum: StatusOfSecondaryEnum

| Name | Value |
|---- | -----|
| AVAILABLE | &quot;Available&quot; |
| UNAVAILABLE | &quot;Unavailable&quot; |



