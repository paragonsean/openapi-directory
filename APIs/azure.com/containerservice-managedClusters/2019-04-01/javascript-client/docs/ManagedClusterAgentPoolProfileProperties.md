# ContainerServiceClient.ManagedClusterAgentPoolProfileProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availabilityZones** | **[String]** | (PREVIEW) Availability zones for nodes. Must use VirtualMachineScaleSets AgentPoolType. | [optional] 
**count** | **Number** | Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.  | [default to 1]
**enableAutoScaling** | **Boolean** | Whether to enable auto-scaler | [optional] 
**maxCount** | **Number** | Maximum number of nodes for auto-scaling | [optional] 
**maxPods** | **Number** | Maximum number of pods that can run on a node. | [optional] 
**minCount** | **Number** | Minimum number of nodes for auto-scaling | [optional] 
**orchestratorVersion** | **String** | Version of orchestrator specified when creating the managed cluster. | [optional] 
**osDiskSizeGB** | **Number** | OS Disk Size in GB to be used to specify the disk size for every machine in this master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified. | [optional] 
**osType** | [**OSType**](OSType.md) |  | [optional] 
**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response. | [optional] [readonly] 
**type** | [**AgentPoolType**](AgentPoolType.md) |  | [optional] 
**vmSize** | [**ContainerServiceVMSize**](ContainerServiceVMSize.md) |  | 
**vnetSubnetID** | **String** | VNet SubnetID specifies the VNet&#39;s subnet identifier. | [optional] 


