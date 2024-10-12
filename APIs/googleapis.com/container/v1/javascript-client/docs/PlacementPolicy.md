# KubernetesEngineApi.PlacementPolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policyName** | **String** | If set, refers to the name of a custom resource policy supplied by the user. The resource policy must be in the same project and region as the node pool. If not found, InvalidArgument error is returned. | [optional] 
**tpuTopology** | **String** | Optional. TPU placement topology for pod slice node pool. https://cloud.google.com/tpu/docs/types-topologies#tpu_topologies | [optional] 
**type** | **String** | The type of placement. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `COMPACT` (value: `"COMPACT"`)




