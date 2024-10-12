# AnthosOnPremApi.BareMetalWorkloadNodeConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**containerRuntime** | **String** | Specifies which container runtime will be used. | [optional] 
**maxPodsPerNode** | **String** | The maximum number of pods a node can run. The size of the CIDR range assigned to the node will be derived from this parameter. | [optional] 



## Enum: ContainerRuntimeEnum


* `CONTAINER_RUNTIME_UNSPECIFIED` (value: `"CONTAINER_RUNTIME_UNSPECIFIED"`)

* `CONTAINERD` (value: `"CONTAINERD"`)




