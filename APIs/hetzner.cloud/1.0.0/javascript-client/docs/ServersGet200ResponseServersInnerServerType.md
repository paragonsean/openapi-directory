# HetznerCloudApi.ServersGet200ResponseServersInnerServerType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cores** | **Number** | Number of cpu cores a Server of this type will have | 
**cpuType** | **String** | Type of cpu | 
**deprecated** | **Boolean** | True if Server type is deprecated | 
**description** | **String** | Description of the Server type | 
**disk** | **Number** | Disk size a Server of this type will have in GB | 
**id** | **Number** | ID of the Server type | 
**memory** | **Number** | Memory a Server of this type will have in GB | 
**name** | **String** | Unique identifier of the Server type | 
**prices** | [**[PricingGet200ResponsePricingServerTypesInnerPricesInner]**](PricingGet200ResponsePricingServerTypesInnerPricesInner.md) | Prices in different Locations | 
**storageType** | **String** | Type of Server boot drive. Local has higher speed. Network has better availability. | 



## Enum: CpuTypeEnum


* `shared` (value: `"shared"`)

* `dedicated` (value: `"dedicated"`)





## Enum: StorageTypeEnum


* `local` (value: `"local"`)

* `network` (value: `"network"`)




