# RudderApi.NodeAddInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agentKey** | [**AgentKey**](AgentKey.md) |  | [optional] 
**hostname** | **String** | The fully qualified name of the node | 
**id** | **String** | The Rudder node unique identifier in /opt/rudder/etc/uuid.hive | 
**ipAddresses** | **[String]** | an array of IPs. | 
**machineType** | **String** | The kind of machine for the node (use vm for a generic VM) | 
**os** | [**Os**](Os.md) |  | 
**policyMode** | **String** | The policy mode for the node. Can only be specified when status&#x3D;accepted. If not specified, the default (global) mode will be used | [optional] 
**policyServerId** | **String** | The policy server ID for that node. By default, \&quot;root\&quot; | [optional] 
**properties** | [**[NodeAddInnerPropertiesInner]**](NodeAddInnerPropertiesInner.md) | Node properties (either set by user or filled by third party sources) | 
**state** | **String** | Node lifecycle state. Can only be specified when status&#x3D;accepted. If not specified, enable is used | [optional] 
**status** | **String** | Target status of the node | 
**timezone** | [**Timezone**](Timezone.md) |  | [optional] 



## Enum: MachineTypeEnum


* `vmware` (value: `"vmware"`)

* `physical` (value: `"physical"`)

* `vm` (value: `"vm"`)

* `solariszone` (value: `"solariszone"`)

* `qemu` (value: `"qemu"`)

* `xen` (value: `"xen"`)

* `aixlpar` (value: `"aixlpar"`)

* `hyperv` (value: `"hyperv"`)

* `bsdjail` (value: `"bsdjail"`)





## Enum: PolicyModeEnum


* `enforce` (value: `"enforce"`)

* `audit` (value: `"audit"`)





## Enum: StateEnum


* `enabled` (value: `"enabled"`)

* `ignored` (value: `"ignored"`)

* `empty-policies` (value: `"empty-policies"`)

* `initializing` (value: `"initializing"`)

* `preparing-eol` (value: `"preparing-eol"`)





## Enum: StatusEnum


* `accepted` (value: `"accepted"`)

* `pending` (value: `"pending"`)




