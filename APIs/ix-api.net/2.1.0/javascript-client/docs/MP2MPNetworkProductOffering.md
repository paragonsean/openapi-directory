# IxApi.MP2MPNetworkProductOffering

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidthMax** | **Number** | When not &#x60;null&#x60;, this value enforces a mandatory rate limit for all network service configs. | 
**bandwidthMin** | **Number** | When configuring access to the network service, at least this &#x60;capacity&#x60; must be provided. | 
**displayName** | **String** |  | 
**downgradeAllowed** | **Boolean** | Indicates if the service can be migrated to a lower bandwidth. | 
**handoverMetroArea** | **String** | Id of the &#x60;MetroArea&#x60;. The network service will be accessed from this metro area.  | 
**handoverMetroAreaNetwork** | **String** | Id of the &#x60;MetroAreaNetwork&#x60;. The service will be accessed through the handover metro area network.  | 
**id** | **String** |  | 
**name** | **String** | Name of the product | 
**physicalPortSpeed** | **Number** | If the service is dependent on the speed of the physical port this field denotes the speed. | 
**providerVlans** | **String** | The &#x60;NetworkService&#x60; provides &#x60;single&#x60; or &#x60;multi&#x60;ple vlans. | 
**resourceType** | **String** | The resource type refers to an ix-api resource.  | 
**serviceMetroArea** | **String** | Id of the &#x60;MetroArea&#x60;. The service is delivered in this metro area.  | 
**serviceMetroAreaNetwork** | **String** | Id of the &#x60;MetroAreaNetwork&#x60;. The service is directly provided on the metro area network.  | 
**serviceProvider** | **String** | The name of the provider providing the service.  | 
**type** | **String** |  | 
**upgradeAllowed** | **Boolean** | Indicates if the service can be migrated to a higher bandwidth. | 



## Enum: ProviderVlansEnum


* `single` (value: `"single"`)

* `multi` (value: `"multi"`)





## Enum: ResourceTypeEnum


* `connection` (value: `"connection"`)

* `demarc` (value: `"demarc"`)

* `network_service` (value: `"network_service"`)

* `network_service_config` (value: `"network_service_config"`)




