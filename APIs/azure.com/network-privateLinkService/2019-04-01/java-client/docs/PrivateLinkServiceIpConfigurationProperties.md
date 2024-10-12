

# PrivateLinkServiceIpConfigurationProperties

Properties of private link service IP configuration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**primary** | **Boolean** | Whether the ip configuration is primary or not. |  [optional] |
|**privateIPAddress** | **String** | The private IP address of the IP configuration. |  [optional] |
|**privateIPAddressVersion** | [**PrivateIPAddressVersionEnum**](#PrivateIPAddressVersionEnum) | IP address version. |  [optional] |
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | IP address allocation method. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**subnet** | [**PrivateLinkServiceIpConfigurationPropertiesSubnet**](PrivateLinkServiceIpConfigurationPropertiesSubnet.md) |  |  [optional] |



## Enum: PrivateIPAddressVersionEnum

| Name | Value |
|---- | -----|
| IPV4 | &quot;IPv4&quot; |
| IPV6 | &quot;IPv6&quot; |



## Enum: PrivateIPAllocationMethodEnum

| Name | Value |
|---- | -----|
| STATIC | &quot;Static&quot; |
| DYNAMIC | &quot;Dynamic&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



