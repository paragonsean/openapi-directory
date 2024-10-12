# KubernetesEngineApi.WorkloadMetadataConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **String** | Mode is the configuration for how to expose metadata to workloads running on the node pool. | [optional] 
**nodeMetadata** | **String** | NodeMetadata is the configuration for how to expose metadata to the workloads running on the node. | [optional] 



## Enum: ModeEnum


* `MODE_UNSPECIFIED` (value: `"MODE_UNSPECIFIED"`)

* `GCE_METADATA` (value: `"GCE_METADATA"`)

* `GKE_METADATA` (value: `"GKE_METADATA"`)





## Enum: NodeMetadataEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `SECURE` (value: `"SECURE"`)

* `EXPOSE` (value: `"EXPOSE"`)

* `GKE_METADATA_SERVER` (value: `"GKE_METADATA_SERVER"`)




