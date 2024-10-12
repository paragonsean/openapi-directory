

# VirtualRouterPropertiesFormat

Virtual Router definition

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hostedGateway** | [**VirtualRouterPropertiesFormatHostedGateway**](VirtualRouterPropertiesFormatHostedGateway.md) |  |  [optional] |
|**hostedSubnet** | [**VirtualRouterPropertiesFormatHostedGateway**](VirtualRouterPropertiesFormatHostedGateway.md) |  |  [optional] |
|**peerings** | [**List&lt;VirtualRouterPropertiesFormatHostedGateway&gt;**](VirtualRouterPropertiesFormatHostedGateway.md) | List of references to VirtualRouterPeerings |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The current provisioning state. |  [optional] [readonly] |
|**virtualRouterAsn** | **Long** | VirtualRouter ASN. |  [optional] |
|**virtualRouterIps** | **List&lt;String&gt;** | VirtualRouter IPs |  [optional] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



