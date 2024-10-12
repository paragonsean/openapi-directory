

# PlacementPolicy

PlacementPolicy defines the placement policy used by the node pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**policyName** | **String** | If set, refers to the name of a custom resource policy supplied by the user. The resource policy must be in the same project and region as the node pool. If not found, InvalidArgument error is returned. |  [optional] |
|**tpuTopology** | **String** | TPU placement topology for pod slice node pool. https://cloud.google.com/tpu/docs/types-topologies#tpu_topologies |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of placement. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| COMPACT | &quot;COMPACT&quot; |



