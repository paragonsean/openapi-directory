

# ApplicationGatewayBackendHealthServerIpConfigurationPropertiesSubnetPropertiesIpConfigurationsInnerProperties

Properties of IP configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateIPAddress** | **String** | The private IP address of the IP configuration. |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | The private IP allocation method. Possible values are &#39;Static&#39; and &#39;Dynamic&#39;. |  [optional] |
|**provisioningState** | **String** | Gets the provisioning state of the public IP resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. |  [optional] |
|**publicIPAddress** | **PublicIPAddress** |  |  [optional] |
|**subnet** | **Subnet** |  |  [optional] |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



