

# OpenShiftManagedClusterAgentPoolProfile

Defines the configuration of the OpenShift cluster VMs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Number of agents (VMs) to host docker containers. |  |
|**name** | **String** | Unique name of the pool profile in the context of the subscription and resource group. |  |
|**osType** | **OSType** |  |  [optional] |
|**role** | **OpenShiftAgentPoolProfileRole** |  |  [optional] |
|**subnetCidr** | **String** | Subnet CIDR for the peering. |  [optional] |
|**vmSize** | **OpenShiftContainerServiceVMSize** |  |  |



