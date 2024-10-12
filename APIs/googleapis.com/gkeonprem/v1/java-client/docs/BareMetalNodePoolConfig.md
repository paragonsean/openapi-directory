

# BareMetalNodePoolConfig

BareMetalNodePoolConfig describes the configuration of all nodes within a given bare metal node pool.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**kubeletConfig** | [**BareMetalKubeletConfig**](BareMetalKubeletConfig.md) |  |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | The labels assigned to nodes of this node pool. An object containing a list of key/value pairs. Example: { \&quot;name\&quot;: \&quot;wrench\&quot;, \&quot;mass\&quot;: \&quot;1.3kg\&quot;, \&quot;count\&quot;: \&quot;3\&quot; }. |  [optional] |
|**nodeConfigs** | [**List&lt;BareMetalNodeConfig&gt;**](BareMetalNodeConfig.md) | Required. The list of machine addresses in the bare metal node pool. |  [optional] |
|**operatingSystem** | [**OperatingSystemEnum**](#OperatingSystemEnum) | Specifies the nodes operating system (default: LINUX). |  [optional] |
|**taints** | [**List&lt;NodeTaint&gt;**](NodeTaint.md) | The initial taints assigned to nodes of this node pool. |  [optional] |



## Enum: OperatingSystemEnum

| Name | Value |
|---- | -----|
| OPERATING_SYSTEM_UNSPECIFIED | &quot;OPERATING_SYSTEM_UNSPECIFIED&quot; |
| LINUX | &quot;LINUX&quot; |



