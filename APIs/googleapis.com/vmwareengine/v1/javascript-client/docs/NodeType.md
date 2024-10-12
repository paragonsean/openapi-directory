# VMwareEngineApi.NodeType

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availableCustomCoreCounts** | **[Number]** | Output only. List of possible values of custom core count. | [optional] [readonly] 
**capabilities** | **[String]** | Output only. Capabilities of this node type. | [optional] [readonly] 
**diskSizeGb** | **Number** | Output only. The amount of storage available, defined in GB. | [optional] [readonly] 
**displayName** | **String** | Output only. The friendly name for this node type. For example: ve1-standard-72 | [optional] [readonly] 
**families** | **[String]** | Output only. Families of the node type. For node types to be in the same cluster they must share at least one element in the &#x60;families&#x60;. | [optional] [readonly] 
**kind** | **String** | Output only. The type of the resource. | [optional] [readonly] 
**memoryGb** | **Number** | Output only. The amount of physical memory available, defined in GB. | [optional] [readonly] 
**name** | **String** | Output only. The resource name of this node type. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-proj/locations/us-central1-a/nodeTypes/standard-72&#x60; | [optional] [readonly] 
**nodeTypeId** | **String** | Output only. The canonical identifier of the node type (corresponds to the &#x60;NodeType&#x60;). For example: standard-72. | [optional] [readonly] 
**totalCoreCount** | **Number** | Output only. The total number of CPU cores in a single node. | [optional] [readonly] 
**virtualCpuCount** | **Number** | Output only. The total number of virtual CPUs in a single node. | [optional] [readonly] 



## Enum: [CapabilitiesEnum]


* `CAPABILITY_UNSPECIFIED` (value: `"CAPABILITY_UNSPECIFIED"`)

* `STRETCHED_CLUSTERS` (value: `"STRETCHED_CLUSTERS"`)





## Enum: KindEnum


* `KIND_UNSPECIFIED` (value: `"KIND_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `STORAGE_ONLY` (value: `"STORAGE_ONLY"`)




