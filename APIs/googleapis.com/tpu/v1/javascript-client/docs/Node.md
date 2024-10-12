# CloudTpuApi.Node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acceleratorType** | **String** | Required. The type of hardware accelerators associated with this node. | [optional] 
**apiVersion** | **String** | Output only. The API version that created this Node. | [optional] [readonly] 
**cidrBlock** | **String** | The CIDR block that the TPU node will use when selecting an IP address. This CIDR block must be a /29 block; the Compute Engine networks API forbids a smaller block, and using a larger block would be wasteful (a node can only consume one IP address). Errors will occur if the CIDR block has already been used for a currently existing TPU node, the CIDR block conflicts with any subnetworks in the user&#39;s provided network, or the provided network is peered with another network that is using that CIDR block. | [optional] 
**createTime** | **String** | Output only. The time when the node was created. | [optional] [readonly] 
**description** | **String** | The user-supplied description of the TPU. Maximum of 512 characters. | [optional] 
**health** | **String** | The health status of the TPU node. | [optional] 
**healthDescription** | **String** | Output only. If this field is populated, it contains a description of why the TPU Node is unhealthy. | [optional] [readonly] 
**ipAddress** | **String** | Output only. DEPRECATED! Use network_endpoints instead. The network address for the TPU Node as visible to Compute Engine instances. | [optional] 
**labels** | **{String: String}** | Resource labels to represent user-provided metadata. | [optional] 
**name** | **String** | Output only. Immutable. The name of the TPU | [optional] [readonly] 
**network** | **String** | The name of a network they wish to peer the TPU node to. It must be a preexisting Compute Engine network inside of the project on which this API has been activated. If none is provided, \&quot;default\&quot; will be used. | [optional] 
**networkEndpoints** | [**[NetworkEndpoint]**](NetworkEndpoint.md) | Output only. The network endpoints where TPU workers can be accessed and sent work. It is recommended that Tensorflow clients of the node reach out to the 0th entry in this map first. | [optional] [readonly] 
**port** | **String** | Output only. DEPRECATED! Use network_endpoints instead. The network port for the TPU Node as visible to Compute Engine instances. | [optional] 
**schedulingConfig** | [**SchedulingConfig**](SchedulingConfig.md) |  | [optional] 
**serviceAccount** | **String** | Output only. The service account used to run the tensor flow services within the node. To share resources, including Google Cloud Storage data, with the Tensorflow job running in the Node, this account must have permissions to that data. | [optional] [readonly] 
**state** | **String** | Output only. The current state for the TPU Node. | [optional] [readonly] 
**symptoms** | [**[Symptom]**](Symptom.md) | Output only. The Symptoms that have occurred to the TPU Node. | [optional] [readonly] 
**tensorflowVersion** | **String** | Required. The version of Tensorflow running in the Node. | [optional] 
**useServiceNetworking** | **Boolean** | Whether the VPC peering for the node is set up through Service Networking API. The VPC Peering should be set up before provisioning the node. If this field is set, cidr_block field should not be specified. If the network, that you want to peer the TPU Node to, is Shared VPC networks, the node must be created with this this field enabled. | [optional] 



## Enum: ApiVersionEnum


* `API_VERSION_UNSPECIFIED` (value: `"API_VERSION_UNSPECIFIED"`)

* `V1_ALPHA1` (value: `"V1_ALPHA1"`)

* `V1` (value: `"V1"`)

* `V2_ALPHA1` (value: `"V2_ALPHA1"`)





## Enum: HealthEnum


* `HEALTH_UNSPECIFIED` (value: `"HEALTH_UNSPECIFIED"`)

* `HEALTHY` (value: `"HEALTHY"`)

* `DEPRECATED_UNHEALTHY` (value: `"DEPRECATED_UNHEALTHY"`)

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




