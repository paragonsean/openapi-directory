

# Node

A TPU instance.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**acceleratorConfig** | [**AcceleratorConfig**](AcceleratorConfig.md) |  |  [optional] |
|**acceleratorType** | **String** | Optional. The type of hardware accelerators associated with this node. |  [optional] |
|**apiVersion** | [**ApiVersionEnum**](#ApiVersionEnum) | Output only. The API version that created this Node. |  [optional] [readonly] |
|**cidrBlock** | **String** | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user&#39;s provided network, or the provided network is peered with another network that is using that CIDR block. |  [optional] |
|**createTime** | **String** | Output only. The time when the node was created. |  [optional] [readonly] |
|**dataDisks** | [**List&lt;AttachedDisk&gt;**](AttachedDisk.md) | The additional data disks for the Node. |  [optional] |
|**description** | **String** | The user-supplied description of the TPU. Maximum of 512 characters. |  [optional] |
|**health** | [**HealthEnum**](#HealthEnum) | The health status of the TPU node. |  [optional] |
|**healthDescription** | **String** | Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. |  [optional] [readonly] |
|**id** | **String** | Output only. The unique identifier for the TPU Node. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Resource labels to represent user-provided metadata. |  [optional] |
|**metadata** | **Map&lt;String, String&gt;** | Custom metadata to apply to the TPU Node. Can set startup-script and shutdown-script |  [optional] |
|**multisliceNode** | **Boolean** | Output only. Whether the Node belongs to a Multislice group. |  [optional] [readonly] |
|**name** | **String** | Output only. Immutable. The name of the TPU. |  [optional] [readonly] |
|**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  |  [optional] |
|**networkEndpoints** | [**List&lt;NetworkEndpoint&gt;**](NetworkEndpoint.md) | Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that runtime clients of the node reach out to the 0th entry in this map first. |  [optional] [readonly] |
|**queuedResource** | **String** | Output only. The qualified name of the QueuedResource that requested this Node. |  [optional] [readonly] |
|**runtimeVersion** | **String** | Required. The runtime version running in the Node. |  [optional] |
|**schedulingConfig** | [**SchedulingConfig**](SchedulingConfig.md) |  |  [optional] |
|**serviceAccount** | [**ServiceAccount**](ServiceAccount.md) |  |  [optional] |
|**shieldedInstanceConfig** | [**ShieldedInstanceConfig**](ShieldedInstanceConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The current state for the TPU Node. |  [optional] [readonly] |
|**symptoms** | [**List&lt;Symptom&gt;**](Symptom.md) | Output only. The Symptoms that have occurred to the TPU Node. |  [optional] [readonly] |
|**tags** | **List&lt;String&gt;** | Tags to apply to the TPU Node. Tags are used to identify valid sources or targets for network firewalls. |  [optional] |



## Enum: ApiVersionEnum

| Name | Value |
|---- | -----|
| API_VERSION_UNSPECIFIED | &quot;API_VERSION_UNSPECIFIED&quot; |
| V1_ALPHA1 | &quot;V1_ALPHA1&quot; |
| V1 | &quot;V1&quot; |
| V2_ALPHA1 | &quot;V2_ALPHA1&quot; |
| V2 | &quot;V2&quot; |



## Enum: HealthEnum

| Name | Value |
|---- | -----|
| HEALTH_UNSPECIFIED | &quot;HEALTH_UNSPECIFIED&quot; |
| HEALTHY | &quot;HEALTHY&quot; |
| TIMEOUT | &quot;TIMEOUT&quot; |
| UNHEALTHY_TENSORFLOW | &quot;UNHEALTHY_TENSORFLOW&quot; |
| UNHEALTHY_MAINTENANCE | &quot;UNHEALTHY_MAINTENANCE&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| RESTARTING | &quot;RESTARTING&quot; |
| REIMAGING | &quot;REIMAGING&quot; |
| DELETING | &quot;DELETING&quot; |
| REPAIRING | &quot;REPAIRING&quot; |
| STOPPED | &quot;STOPPED&quot; |
| STOPPING | &quot;STOPPING&quot; |
| STARTING | &quot;STARTING&quot; |
| PREEMPTED | &quot;PREEMPTED&quot; |
| TERMINATED | &quot;TERMINATED&quot; |
| HIDING | &quot;HIDING&quot; |
| HIDDEN | &quot;HIDDEN&quot; |
| UNHIDING | &quot;UNHIDING&quot; |



