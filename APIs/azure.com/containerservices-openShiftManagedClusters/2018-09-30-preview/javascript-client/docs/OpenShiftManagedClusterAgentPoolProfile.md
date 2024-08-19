# ContainerServiceClient.OpenShiftManagedClusterAgentPoolProfile

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **Number** | Number of agents (VMs) to host docker containers. | 
**name** | **String** | Unique name of the pool profile in the context of the subscription and resource group. | 
**osType** | [**OSType**](OSType.md) |  | [optional] 
**role** | [**OpenShiftAgentPoolProfileRole**](OpenShiftAgentPoolProfileRole.md) |  | [optional] 
**subnetCidr** | **String** | Subnet CIDR for the peering. | [optional] [default to &#39;10.0.0.0/24&#39;]
**vmSize** | [**OpenShiftContainerServiceVMSize**](OpenShiftContainerServiceVMSize.md) |  | 


