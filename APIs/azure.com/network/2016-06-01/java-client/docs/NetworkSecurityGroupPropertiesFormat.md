

# NetworkSecurityGroupPropertiesFormat

Network Security Group resource

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**defaultSecurityRules** | [**List&lt;SecurityRule&gt;**](SecurityRule.md) | Gets or default security rules of network security group |  [optional] |
|**networkInterfaces** | [**List&lt;NetworkInterface&gt;**](NetworkInterface.md) | Gets collection of references to Network Interfaces |  [optional] [readonly] |
|**provisioningState** | **String** | Gets provisioning state of the PublicIP resource Updating/Deleting/Failed |  [optional] |
|**resourceGuid** | **String** | Gets or sets resource guid property of the network security group resource |  [optional] |
|**securityRules** | [**List&lt;SecurityRule&gt;**](SecurityRule.md) | Gets or sets security rules of network security group |  [optional] |
|**subnets** | [**List&lt;Subnet&gt;**](Subnet.md) | Gets collection of references to subnets |  [optional] [readonly] |



