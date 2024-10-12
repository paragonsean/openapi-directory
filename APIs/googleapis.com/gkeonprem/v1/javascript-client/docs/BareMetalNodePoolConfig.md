# AnthosOnPremApi.BareMetalNodePoolConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubeletConfig** | [**BareMetalKubeletConfig**](BareMetalKubeletConfig.md) |  | [optional] 
**labels** | **{String: String}** | The labels assigned to nodes of this node pool. An object containing a list of key/value pairs. Example: { \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }. | [optional] 
**nodeConfigs** | [**[BareMetalNodeConfig]**](BareMetalNodeConfig.md) | Required. The list of machine addresses in the bare metal node pool. | [optional] 
**operatingSystem** | **String** | Specifies the nodes operating system (default: LINUX). | [optional] 
**taints** | [**[NodeTaint]**](NodeTaint.md) | The initial taints assigned to nodes of this node pool. | [optional] 



## Enum: OperatingSystemEnum


* `OPERATING_SYSTEM_UNSPECIFIED` (value: `"OPERATING_SYSTEM_UNSPECIFIED"`)

* `LINUX` (value: `"LINUX"`)




