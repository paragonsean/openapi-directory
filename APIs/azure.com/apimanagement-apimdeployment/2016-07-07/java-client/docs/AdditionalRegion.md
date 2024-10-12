

# AdditionalRegion

Description of an additional API Management resource location.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**location** | **String** | The location name of the additional region among Azure Data center regions. |  |
|**skuType** | [**SkuTypeEnum**](#SkuTypeEnum) | The SKU type in the location. |  |
|**skuUnitCount** | **Integer** | The SKU Unit count at the location. The maximum SKU Unit count depends on the SkuType. Maximum allowed for Developer SKU is 1, for Standard SKU is 4, and for Premium SKU is 10, at a location. |  [optional] |
|**staticIPs** | **List&lt;String&gt;** | Static IP addresses of the location&#39;s virtual machines. |  [optional] [readonly] |
|**vpnconfiguration** | [**VirtualNetworkConfiguration**](VirtualNetworkConfiguration.md) |  |  [optional] |



## Enum: SkuTypeEnum

| Name | Value |
|---- | -----|
| DEVELOPER | &quot;Developer&quot; |
| STANDARD | &quot;Standard&quot; |
| PREMIUM | &quot;Premium&quot; |



