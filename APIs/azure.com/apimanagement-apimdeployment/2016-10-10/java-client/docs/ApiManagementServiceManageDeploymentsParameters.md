

# ApiManagementServiceManageDeploymentsParameters

Parameters supplied to the ManageDeployments operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalLocations** | [**List&lt;AdditionalRegion&gt;**](AdditionalRegion.md) | Additional data center locations for the API Management service. |  [optional] |
|**location** | **String** | Location of the API Management service Azure data center. |  |
|**skuType** | [**SkuTypeEnum**](#SkuTypeEnum) | SKU type of the API Management service. |  |
|**skuUnitCount** | **Integer** | SKU Unit count of the API Management service. Default value is 1. |  [optional] |
|**vpnConfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  |  [optional] |
|**vpnType** | [**VpnTypeEnum**](#VpnTypeEnum) | The type of VPN in which API Management service needs to be configured in. None (Default Value) means the API Management service is not part of any Virtual Network, External means the API Management deployment is set up inside a Virtual Network having an Internet Facing Endpoint, and Internal means that the API Management service deployment is set up inside a Virtual Network having an Intranet Facing Endpoint only. When vpnConfiguration is specified, vpnType must be specified. |  [optional] |



## Enum: SkuTypeEnum

| Name | Value |
|---- | -----|
| DEVELOPER | &quot;Developer&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



## Enum: VpnTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| EXTERNAL | &quot;External&quot; |
| INTERNAL | &quot;Internal&quot; |



