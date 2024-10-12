

# BareMetalWorkloadNodeConfig

Specifies the workload node configurations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerRuntime** | [**ContainerRuntimeEnum**](#ContainerRuntimeEnum) | Specifies which container runtime will be used. |  [optional] |
|**maxPodsPerNode** | **String** | The maximum number of pods a node can run. The size of the CIDR range assigned to the node will be derived from this parameter. |  [optional] |



## Enum: ContainerRuntimeEnum

| Name | Value |
|---- | -----|
| CONTAINER_RUNTIME_UNSPECIFIED | &quot;CONTAINER_RUNTIME_UNSPECIFIED&quot; |
| CONTAINERD | &quot;CONTAINERD&quot; |



