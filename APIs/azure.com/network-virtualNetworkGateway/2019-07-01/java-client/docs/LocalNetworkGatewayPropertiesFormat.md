

# LocalNetworkGatewayPropertiesFormat

LocalNetworkGateway properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bgpSettings** | [**BgpSettings**](BgpSettings.md) |  |  [optional] |
|**gatewayIpAddress** | **String** | IP address of local network gateway. |  [optional] |
|**localNetworkAddressSpace** | [**LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace**](LocalNetworkGatewayPropertiesFormatLocalNetworkAddressSpace.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**resourceGuid** | **String** | The resource GUID property of the local network gateway resource. |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



