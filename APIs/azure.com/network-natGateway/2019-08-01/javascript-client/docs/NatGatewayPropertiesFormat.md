# NetworkManagementClient.NatGatewayPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idleTimeoutInMinutes** | **Number** | The idle timeout of the nat gateway. | [optional] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**publicIpAddresses** | [**[NatGatewayPropertiesFormatPublicIpAddressesInner]**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of public ip addresses associated with the nat gateway resource. | [optional] 
**publicIpPrefixes** | [**[NatGatewayPropertiesFormatPublicIpAddressesInner]**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of public ip prefixes associated with the nat gateway resource. | [optional] 
**resourceGuid** | **String** | The resource GUID property of the NAT gateway resource. | [optional] 
**subnets** | [**[NatGatewayPropertiesFormatPublicIpAddressesInner]**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of references to the subnets using this nat gateway resource. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




