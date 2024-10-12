

# WorkloadMetadataConfig

WorkloadMetadataConfig defines the metadata configuration to expose to workloads on the node pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) | Mode is the configuration for how to expose metadata to workloads running on the node pool. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| GCE_METADATA | &quot;GCE_METADATA&quot; |
| GKE_METADATA | &quot;GKE_METADATA&quot; |



