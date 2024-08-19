

# OpenShiftManagedClusterMasterPoolProfile

OpenShiftManagedClusterMaterPoolProfile contains configuration for OpenShift master VMs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**count** | **Integer** | Number of masters (VMs) to host docker containers. The default value is 3. |  |
|**name** | **String** | Unique name of the master pool profile in the context of the subscription and resource group. |  [optional] |
|**osType** | **OSType** |  |  [optional] |
|**subnetCidr** | **String** | Subnet CIDR for the peering. |  [optional] |
|**vmSize** | **OpenShiftContainerServiceVMSize** |  |  |



