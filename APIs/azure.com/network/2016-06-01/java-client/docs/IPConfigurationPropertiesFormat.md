

# IPConfigurationPropertiesFormat

Properties of IPConfiguration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateIPAddress** | **String** | Gets or sets the privateIPAddress of the IP Configuration |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | Gets or sets PrivateIP allocation method |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**publicIPAddress** | [**PublicIPAddress**](PublicIPAddress.md) |  |  [optional] |
|**subnet** | [**Subnet**](Subnet.md) |  |  [optional] |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



