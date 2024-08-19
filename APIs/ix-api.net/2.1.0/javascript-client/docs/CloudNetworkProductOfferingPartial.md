# IxApi.CloudNetworkProductOfferingPartial

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidthMax** | **Number** | When not &#x60;null&#x60;, this value enforces a mandatory rate limit for all network service configs. | [optional] 
**bandwidthMin** | **Number** | When configuring access to the network service, at least this &#x60;capacity&#x60; must be provided. | [optional] 
**deliveryMethod** | **String** | The exchange delivers the service over a &#x60;shared&#x60; or &#x60;dedicated&#x60; NNI. | [optional] 
**displayName** | **String** |  | [optional] 
**diversity** | **Number** | The service can be delivered over multiple handovers from the exchange to the &#x60;service_provider&#x60;. The &#x60;diversity&#x60; denotes the number of handovers between the exchange and the service provider. A value of two signals a redundant service.  Only one network service configuration for each &#x60;handover&#x60; and &#x60;cloud_vlan&#x60; can be created. | [optional] 
**downgradeAllowed** | **Boolean** | Indicates if the service can be migrated to a lower bandwidth. | [optional] 
**handoverMetroArea** | **String** | Id of the &#x60;MetroArea&#x60;. The network service will be accessed from this metro area.  | [optional] 
**handoverMetroAreaNetwork** | **String** | Id of the &#x60;MetroAreaNetwork&#x60;. The service will be accessed through the handover metro area network.  | [optional] 
**id** | **String** |  | [optional] 
**name** | **String** | Name of the product | [optional] 
**physicalPortSpeed** | **Number** | If the service is dependent on the speed of the physical port this field denotes the speed. | [optional] 
**providerVlans** | **String** | The &#x60;NetworkService&#x60; provides &#x60;single&#x60; or &#x60;multi&#x60;ple vlans. | [optional] 
**resourceType** | **String** | The resource type refers to an ix-api resource.  | [optional] 
**serviceMetroArea** | **String** | Id of the &#x60;MetroArea&#x60;. The service is delivered in this metro area.  | [optional] 
**serviceMetroAreaNetwork** | **String** | Id of the &#x60;MetroAreaNetwork&#x60;. The service is directly provided on the metro area network.  | [optional] 
**serviceProvider** | **String** | The name of the provider providing the service.  | [optional] 
**serviceProviderPop** | **String** | The datacenter description of the partner NNI to the service provider.  | [optional] 
**serviceProviderRegion** | **String** | The service provider offers the network service for a specific region.  | [optional] 
**serviceProviderWorkflow** | **String** | When the workflow is &#x60;provider_first&#x60; the subscriber creates a circuit with the cloud provider and provides a &#x60;cloud_key&#x60; for filtering the product-offerings.  If the workflow is &#x60;exchange_first&#x60; the IX will create the cloud circuit on the provider side.  | [optional] 
**type** | **String** |  | 
**upgradeAllowed** | **Boolean** | Indicates if the service can be migrated to a higher bandwidth. | [optional] 



## Enum: DeliveryMethodEnum


* `dedicated` (value: `"dedicated"`)

* `shared` (value: `"shared"`)





## Enum: ProviderVlansEnum


* `single` (value: `"single"`)

* `multi` (value: `"multi"`)





## Enum: ResourceTypeEnum


* `connection` (value: `"connection"`)

* `demarc` (value: `"demarc"`)

* `network_service` (value: `"network_service"`)

* `network_service_config` (value: `"network_service_config"`)





## Enum: ServiceProviderWorkflowEnum


* `exchange_first` (value: `"exchange_first"`)

* `provider_first` (value: `"provider_first"`)




