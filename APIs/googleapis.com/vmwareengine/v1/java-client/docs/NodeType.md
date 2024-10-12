

# NodeType

Describes node type.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**availableCustomCoreCounts** | **List&lt;Integer&gt;** | Output only. List of possible values of custom core count. |  [optional] [readonly] |
|**capabilities** | [**List&lt;CapabilitiesEnum&gt;**](#List&lt;CapabilitiesEnum&gt;) | Output only. Capabilities of this node type. |  [optional] [readonly] |
|**diskSizeGb** | **Integer** | Output only. The amount of storage available, defined in GB. |  [optional] [readonly] |
|**displayName** | **String** | Output only. The friendly name for this node type. For example: ve1-standard-72 |  [optional] [readonly] |
|**families** | **List&lt;String&gt;** | Output only. Families of the node type. For node types to be in the same cluster they must share at least one element in the &#x60;families&#x60;. |  [optional] [readonly] |
|**kind** | [**KindEnum**](#KindEnum) | Output only. The type of the resource. |  [optional] [readonly] |
|**memoryGb** | **Integer** | Output only. The amount of physical memory available, defined in GB. |  [optional] [readonly] |
|**name** | **String** | Output only. The resource name of this node type. Resource names are schemeless URIs that follow the conventions in https://cloud.google.com/apis/design/resource_names. For example: &#x60;projects/my-proj/locations/us-central1-a/nodeTypes/standard-72&#x60; |  [optional] [readonly] |
|**nodeTypeId** | **String** | Output only. The canonical identifier of the node type (corresponds to the &#x60;NodeType&#x60;). For example: standard-72. |  [optional] [readonly] |
|**totalCoreCount** | **Integer** | Output only. The total number of CPU cores in a single node. |  [optional] [readonly] |
|**virtualCpuCount** | **Integer** | Output only. The total number of virtual CPUs in a single node. |  [optional] [readonly] |



## Enum: List&lt;CapabilitiesEnum&gt;

| Name | Value |
|---- | -----|
| CAPABILITY_UNSPECIFIED | &quot;CAPABILITY_UNSPECIFIED&quot; |
| STRETCHED_CLUSTERS | &quot;STRETCHED_CLUSTERS&quot; |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| KIND_UNSPECIFIED | &quot;KIND_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| STORAGE_ONLY | &quot;STORAGE_ONLY&quot; |



