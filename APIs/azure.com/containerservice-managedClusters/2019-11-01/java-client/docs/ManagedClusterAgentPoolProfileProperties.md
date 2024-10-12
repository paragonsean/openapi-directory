

# ManagedClusterAgentPoolProfileProperties

Properties for the container service agent pool profile.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availabilityZones** | **List&lt;String&gt;** | Availability zones for nodes. Must use VirtualMachineScaleSets AgentPoolType. |  [optional] |
|**count** | **Integer** | Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.  |  |
|**enableAutoScaling** | **Boolean** | Whether to enable auto-scaler |  [optional] |
|**enableNodePublicIP** | **Boolean** | Enable public IP for nodes |  [optional] |
|**maxCount** | **Integer** | Maximum number of nodes for auto-scaling |  [optional] |
|**maxPods** | **Integer** | Maximum number of pods that can run on a node. |  [optional] |
|**minCount** | **Integer** | Minimum number of nodes for auto-scaling |  [optional] |
|**nodeLabels** | **Map&lt;String, String&gt;** | Agent pool node labels to be persisted across all nodes in agent pool. |  [optional] |
|**nodeTaints** | **List&lt;String&gt;** | Taints added to new nodes during node pool create and scale. For example, key&#x3D;value:NoSchedule. |  [optional] |
|**orchestratorVersion** | **String** | Version of orchestrator specified when creating the managed cluster. |  [optional] |
|**osDiskSizeGB** | **Integer** | OS Disk Size in GB to be used to specify the disk size for every machine in this master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified. |  [optional] |
|**osType** | **OSType** |  |  [optional] |
|**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response. |  [optional] [readonly] |
|**scaleSetEvictionPolicy** | **ScaleSetEvictionPolicy** |  |  [optional] |
|**scaleSetPriority** | **ScaleSetPriority** |  |  [optional] |
|**tags** | **Map&lt;String, String&gt;** | Agent pool tags to be persisted on the agent pool virtual machine scale set. |  [optional] |
|**type** | **AgentPoolType** |  |  [optional] |
|**vmSize** | **ContainerServiceVMSize** |  |  |
|**vnetSubnetID** | **String** | VNet SubnetID specifies the VNet&#39;s subnet identifier. |  [optional] |



