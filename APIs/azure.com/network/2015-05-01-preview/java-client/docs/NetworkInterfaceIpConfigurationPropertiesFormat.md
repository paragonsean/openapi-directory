

# NetworkInterfaceIpConfigurationPropertiesFormat

Properties of IPConfiguration

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**loadBalancerBackendAddressPools** | [**List&lt;SubResource&gt;**](SubResource.md) | Gets or sets the reference of LoadBalancerBackendAddressPool resource |  [optional] |
|**loadBalancerInboundNatRules** | [**List&lt;SubResource&gt;**](SubResource.md) | Gets or sets list of references of LoadBalancerInboundNatRules |  [optional] |
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



