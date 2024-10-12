# ApiManagementClient.ApiManagementServiceManageDeploymentsParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additionalLocations** | [**[AdditionalRegion]**](AdditionalRegion.md) | Additional data center locations for the API Management service. | [optional] 
**location** | **String** | Location of the API Management service Azure data center. | 
**skuType** | **String** | SKU type of the API Management service. | 
**skuUnitCount** | **Number** | SKU Unit count of the API Management service. Default value is 1. | [optional] [default to 1]
**vpnConfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  | [optional] 
**vpnType** | **String** | The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that the API Management service deployment is set up inside a Virtual Network having an Intranet Facing Endpoint only. When vpnConfiguration is specified, vpnType must be specified. | [optional] [default to &#39;None&#39;]



## Enum: SkuTypeEnum


* `Developer` (value: `"Developer"`)

* `Standard` (value: `"Standard"`)

* `Premium` (value: `"Premium"`)





## Enum: VpnTypeEnum


* `None` (value: `"None"`)

* `External` (value: `"External"`)

* `Internal` (value: `"Internal"`)




