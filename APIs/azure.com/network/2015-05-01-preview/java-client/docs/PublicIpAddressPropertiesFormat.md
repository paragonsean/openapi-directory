

# PublicIpAddressPropertiesFormat

PublicIpAddress properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsSettings** | [**PublicIpAddressDnsSettings**](PublicIpAddressDnsSettings.md) |  |  [optional] |
|**idleTimeoutInMinutes** | **Integer** | Gets or sets the idle timeout of the public IP address |  [optional] |
|**ipAddress** | **String** | Gets the assigned public IP address |  [optional] |
|**ipConfiguration** | [**SubResource**](SubResource.md) |  |  [optional] |
|**provisioningState** | **String** | Gets or sets Provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**publicIPAllocationMethod** | [**PublicIPAllocationMethodEnum**](#PublicIPAllocationMethodEnum) | Gets or sets PublicIP allocation method (Static/Dynamic) |  |
|**resourceGuid** | **String** | Gets or sets resource guid property of the PublicIP resource |  [optional] |



## Enum: PublicIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



