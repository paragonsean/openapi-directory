

# ApplicationGatewayBackendAddressPoolPropertiesFormat

Properties of Backend Address Pool of an application gateway.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backendAddresses** | [**List&lt;ApplicationGatewayBackendAddress&gt;**](ApplicationGatewayBackendAddress.md) | Backend addresses. |  [optional] |
|**backendIPConfigurations** | [**List&lt;ApplicationGatewayBackendHealthServerIpConfiguration&gt;**](ApplicationGatewayBackendHealthServerIpConfiguration.md) | Collection of references to IPs defined in network interfaces. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



