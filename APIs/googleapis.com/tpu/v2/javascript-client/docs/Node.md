# CloudTpuApi.Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceleratorConfig** | [**AcceleratorConfig**](AcceleratorConfig.md) |  | [optional] 
**acceleratorType** | **String** | Optional. The type of hardware accelerators associated with this node. | [optional] 
**apiVersion** | **String** | Output only. The API version that created this Node. | [optional] [readonly] 
**cidrBlock** | **String** | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user&#39;s provided network, or the provided network is peered with another network that is using that CIDR block. | [optional] 
**createTime** | **String** | Output only. The time when the node was created. | [optional] [readonly] 
**dataDisks** | [**[AttachedDisk]**](AttachedDisk.md) | The additional data disks for the Node. | [optional] 
**description** | **String** | The user-supplied description of the TPU. Maximum of 512 characters. | [optional] 
**health** | **String** | The health status of the TPU node. | [optional] 
**healthDescription** | **String** | Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. | [optional] [readonly] 
**id** | **String** | Output only. The unique identifier for the TPU Node. | [optional] [readonly] 
**labels** | **{String: String}** | Resource labels to represent user-provided metadata. | [optional] 
**metadata** | **{String: String}** | Custom metadata to apply to the TPU Node. Can set startup-script and shutdown-script | [optional] 
**multisliceNode** | **Boolean** | Output only. Whether the Node belongs to a Multislice group. | [optional] [readonly] 
**name** | **String** | Output only. Immutable. The name of the TPU. | [optional] [readonly] 
**networkConfig** | [**NetworkConfig**](NetworkConfig.md) |  | [optional] 
**networkEndpoints** | [**[NetworkEndpoint]**](NetworkEndpoint.md) | Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that runtime clients of the node reach out to the 0th entry in this map first. | [optional] [readonly] 
**queuedResource** | **String** | Output only. The qualified name of the QueuedResource that requested this Node. | [optional] [readonly] 
**runtimeVersion** | **String** | Required. The runtime version running in the Node. | [optional] 
**schedulingConfig** | [**SchedulingConfig**](SchedulingConfig.md) |  | [optional] 
**serviceAccount** | [**ServiceAccount**](ServiceAccount.md) |  | [optional] 
**shieldedInstanceConfig** | [**ShieldedInstanceConfig**](ShieldedInstanceConfig.md) |  | [optional] 
**state** | **String** | Output only. The current state for the TPU Node. | [optional] [readonly] 
**symptoms** | [**[Symptom]**](Symptom.md) | Output only. The Symptoms that have occurred to the TPU Node. | [optional] [readonly] 
**tags** | **[String]** | Tags to apply to the TPU Node. Tags are used to identify valid sources or targets for network firewalls. | [optional] 



## Enum: ApiVersionEnum


* `API_VERSION_UNSPECIFIED` (value: `"API_VERSION_UNSPECIFIED"`)

* `V1_ALPHA1` (value: `"V1_ALPHA1"`)

* `V1` (value: `"V1"`)

* `V2_ALPHA1` (value: `"V2_ALPHA1"`)

* `V2` (value: `"V2"`)





## Enum: HealthEnum


* `HEALTH_UNSPECIFIED` (value: `"HEALTH_UNSPECIFIED"`)

* `HEALTHY` (value: `"HEALTHY"`)

* `TIMEOUT` (value: `"TIMEOUT"`)

* `UNHEALTHY_TENSORFLOW` (value: `"UNHEALTHY_TENSORFLOW"`)

* `UNHEALTHY_MAINTENANCE` (value: `"UNHEALTHY_MAINTENANCE"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `RESTARTING` (value: `"RESTARTING"`)

* `REIMAGING` (value: `"REIMAGING"`)

* `DELETING` (value: `"DELETING"`)

* `REPAIRING` (value: `"REPAIRING"`)

* `STOPPED` (value: `"STOPPED"`)

* `STOPPING` (value: `"STOPPING"`)

* `STARTING` (value: `"STARTING"`)

* `PREEMPTED` (value: `"PREEMPTED"`)

* `TERMINATED` (value: `"TERMINATED"`)

* `HIDING` (value: `"HIDING"`)

* `HIDDEN` (value: `"HIDDEN"`)

* `UNHIDING` (value: `"UNHIDING"`)




