

# VirtualNetworkGatewayIPConfigurationPropertiesFormat

Properties of VirtualNetworkGatewayIPConfiguration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateIPAddress** | **String** | Gets or sets the privateIPAddress of the IP Configuration |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | The private IP allocation method. Possible values are: &#39;Static&#39; and &#39;Dynamic&#39;. |  [optional] |
|**provisioningState** | **String** | The provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddress** | [**VirtualNetworkGatewayConnectionPropertiesFormatPeer**](VirtualNetworkGatewayConnectionPropertiesFormatPeer.md) |  |  [optional] |
|**subnet** | [**VirtualNetworkGatewayConnectionPropertiesFormatPeer**](VirtualNetworkGatewayConnectionPropertiesFormatPeer.md) |  |  [optional] |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



