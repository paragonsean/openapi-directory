

# BastionHostIPConfigurationPropertiesFormat

Properties of IP configuration of an Bastion Host.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**privateIPAllocationMethod** | [**PrivateIPAllocationMethodEnum**](#PrivateIPAllocationMethodEnum) | IP address allocation method. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**publicIPAddress** | [**BastionHostIPConfigurationPropertiesFormatPublicIPAddress**](BastionHostIPConfigurationPropertiesFormatPublicIPAddress.md) |  |  |
|**subnet** | [**BastionHostIPConfigurationPropertiesFormatPublicIPAddress**](BastionHostIPConfigurationPropertiesFormatPublicIPAddress.md) |  |  |



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



