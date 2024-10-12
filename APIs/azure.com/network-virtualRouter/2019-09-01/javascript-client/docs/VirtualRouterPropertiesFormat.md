# NetworkManagementClient.VirtualRouterPropertiesFormat

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostedGateway** | [**VirtualRouterPropertiesFormatHostedGateway**](VirtualRouterPropertiesFormatHostedGateway.md) |  | [optional] 
**hostedSubnet** | [**VirtualRouterPropertiesFormatHostedGateway**](VirtualRouterPropertiesFormatHostedGateway.md) |  | [optional] 
**peerings** | [**[VirtualRouterPropertiesFormatHostedGateway]**](VirtualRouterPropertiesFormatHostedGateway.md) | List of references to VirtualRouterPeerings. | [optional] [readonly] 
**provisioningState** | **String** | The current provisioning state. | [optional] [readonly] 
**virtualRouterAsn** | **Number** | VirtualRouter ASN. | [optional] 
**virtualRouterIps** | **[String]** | VirtualRouter IPs. | [optional] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




