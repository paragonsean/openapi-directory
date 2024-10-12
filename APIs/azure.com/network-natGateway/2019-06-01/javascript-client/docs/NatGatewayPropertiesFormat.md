# NetworkManagementClient.NatGatewayPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idleTimeoutInMinutes** | **Number** | The idle timeout of the nat gateway. | [optional] 
**provisioningState** | **String** | The provisioning state of the NatGateway resource. Possible values are: &#39;Updating&#39;, &#39;Deleting&#39;, and &#39;Failed&#39;. | [optional] 
**publicIpAddresses** | [**[NatGatewayPropertiesFormatPublicIpAddressesInner]**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of public ip addresses associated with the nat gateway resource. | [optional] 
**publicIpPrefixes** | [**[NatGatewayPropertiesFormatPublicIpAddressesInner]**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of public ip prefixes associated with the nat gateway resource. | [optional] 
**resourceGuid** | **String** | The resource GUID property of the nat gateway resource. | [optional] 
**subnets** | [**[NatGatewayPropertiesFormatPublicIpAddressesInner]**](NatGatewayPropertiesFormatPublicIpAddressesInner.md) | An array of references to the subnets using this nat gateway resource. | [optional] [readonly] 


