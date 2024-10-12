

# VirtualNetworkGatewayIpConfigurationPropertiesFormat

Properties of VirtualNetworkGatewayIPConfiguration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateIPAddress** | **String** | Gets or sets the privateIPAddress of the Network Interface IP Configuration |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | Gets or sets PrivateIP allocation method (Static/Dynamic) |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**publicIPAddress** | [**SubResource**](SubResource.md) |  |  [optional] |
|**subnet** | [**SubResource**](SubResource.md) |  |  [optional] |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



