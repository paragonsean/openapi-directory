

# NatGatewayPropertiesFormat

Nat Gateway properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**idleTimeoutInMinutes** | **Integer** | The idle timeout of the nat gateway. |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**publicIpAddresses** | [**List&lt;NatGatewayPropertiesFormatPublicIpAddressesInner&gt;**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of public ip addresses associated with the nat gateway resource. |  [optional] |
|**publicIpPrefixes** | [**List&lt;NatGatewayPropertiesFormatPublicIpAddressesInner&gt;**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of public ip prefixes associated with the nat gateway resource. |  [optional] |
|**resourceGuid** | **String** | The resource GUID property of the NAT gateway resource. |  [optional] |
|**subnets** | [**List&lt;NatGatewayPropertiesFormatPublicIpAddressesInner&gt;**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of references to the subnets using this nat gateway resource. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



