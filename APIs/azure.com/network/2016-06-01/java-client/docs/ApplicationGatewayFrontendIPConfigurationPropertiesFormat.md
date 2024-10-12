

# ApplicationGatewayFrontendIPConfigurationPropertiesFormat

Properties of Frontend IP configuration of application gateway

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateIPAddress** | **String** | PrivateIPAddress of the Network Interface IP Configuration |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | PrivateIP allocation method (Static/Dynamic) |  [optional] |
|**provisioningState** | **String** | Provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**publicIPAddress** | [**SubResource**](SubResource.md) |  |  [optional] |
|**subnet** | [**SubResource**](SubResource.md) |  |  [optional] |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



