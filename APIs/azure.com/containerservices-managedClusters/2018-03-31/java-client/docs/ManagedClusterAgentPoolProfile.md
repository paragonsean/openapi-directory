

# ManagedClusterAgentPoolProfile

Profile for the container service agent pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1.  |  [optional] |
|**maxPods** | **Integer** | Maximum number of pods that can run on a node. |  [optional] |
|**name** | **String** | Unique name of the agent pool profile in the context of the subscription and resource group. |  |
|**osDiskSizeGB** | **Integer** | OS Disk Size in GB to be used to specify the disk size for every machine in this master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified. |  [optional] |
|**osType** | **OSType** |  |  [optional] |
|**storageProfile** | **ContainerServiceStorageProfile** |  |  [optional] |
|**vmSize** | **ContainerServiceVMSize** |  |  |
|**vnetSubnetID** | **String** | VNet SubnetID specifies the VNet&#39;s subnet identifier. |  [optional] |



