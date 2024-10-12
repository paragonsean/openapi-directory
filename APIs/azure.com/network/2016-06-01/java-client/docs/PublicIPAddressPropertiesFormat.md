

# PublicIPAddressPropertiesFormat

PublicIpAddress properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dnsSettings** | [**PublicIPAddressDnsSettings**](PublicIPAddressDnsSettings.md) |  |  [optional] |
|**idleTimeoutInMinutes** | **Integer** | Gets or sets the idle timeout of the public IP address |  [optional] |
|**ipAddress** | **String** |  |  [optional] |
|**ipConfiguration** | [**IPConfiguration**](IPConfiguration.md) |  |  [optional] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**publicIPAddressVersion** | [**PublicIPAddressVersionEnum**](#PublicIPAddressVersionEnum) | Gets or sets PublicIP address version (IPv4/IPv6) |  [optional] |
|**publicIPAllocationMethod** | [**PublicIPAllocationMethodEnum**](#PublicIPAllocationMethodEnum) | Gets or sets PublicIP allocation method (Static/Dynamic) |  [optional] |
|**resourceGuid** | **String** | Gets or sets resource guid property of the PublicIP resource |  [optional] |



## Enum: PublicIPAddressVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



## Enum: PublicIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



