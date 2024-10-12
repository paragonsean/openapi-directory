

# WorkloadMetadataConfig

WorkloadMetadataConfig defines the metadata configuration to expose to workloads on the node pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mode** | [**ModeEnum**](#ModeEnum) | Mode is the configuration for how to expose metadata to workloads running on the node pool. |  [optional] |
|**nodeMetadata** | [**NodeMetadataEnum**](#NodeMetadataEnum) | NodeMetadata is the configuration for how to expose metadata to the workloads running on the node. |  [optional] |



## Enum: ModeEnum

| Name | Value |
|---- | -----|
| MODE_UNSPECIFIED | &quot;MODE_UNSPECIFIED&quot; |
| GCE_METADATA | &quot;GCE_METADATA&quot; |
| GKE_METADATA | &quot;GKE_METADATA&quot; |



## Enum: NodeMetadataEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| SECURE | &quot;SECURE&quot; |
| EXPOSE | &quot;EXPOSE&quot; |
| GKE_METADATA_SERVER | &quot;GKE_METADATA_SERVER&quot; |



