

# VmwareControlPlaneNodeConfig

Specifies control plane node config for the VMware user cluster.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoResizeConfig** | [**VmwareAutoResizeConfig**](VmwareAutoResizeConfig.md) |  |  [optional] |
|**cpus** | **String** | The number of CPUs for each admin cluster node that serve as control planes for this VMware user cluster. (default: 4 CPUs) |  [optional] |
|**memory** | **String** | The megabytes of memory for each admin cluster node that serves as a control plane for this VMware user cluster (default: 8192 MB memory). |  [optional] |
|**replicas** | **String** | The number of control plane nodes for this VMware user cluster. (default: 1 replica). |  [optional] |
|**vsphereConfig** | [**VmwareControlPlaneVsphereConfig**](VmwareControlPlaneVsphereConfig.md) |  |  [optional] |



