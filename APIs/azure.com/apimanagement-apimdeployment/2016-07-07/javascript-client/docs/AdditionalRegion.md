# ApiManagementClient.AdditionalRegion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **String** | The location name of the additional region among Azure Data center regions. | 
**skuType** | **String** | The SKU type in the location. | 
**skuUnitCount** | **Number** | The SKU Unit count at the location. The maximum SKU Unit count depends on the SkuType. Maximum allowed for Developer SKU is 1, for Standard SKU is 4, and for Premium SKU is 10, at a location. | [optional] [default to 1]
**staticIPs** | **[String]** | Static IP addresses of the location&#39;s virtual machines. | [optional] [readonly] 
**vpnconfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  | [optional] 



## Enum: SkuTypeEnum


* `Developer` (value: `"Developer"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)




