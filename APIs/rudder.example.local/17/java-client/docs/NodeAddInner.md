

# NodeAddInner


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**agentKey** | [**AgentKey**](AgentKey.md) |  |  [optional] |
|**hostname** | **String** | The fully qualified name of the node |  |
|**id** | **String** | The Rudder node unique identifier in /opt/rudder/etc/uuid.hive |  |
|**ipAddresses** | **List&lt;String&gt;** | an array of IPs. |  |
|**machineType** | [**MachineTypeEnum**](#MachineTypeEnum) | The kind of machine for the node (use vm for a generic VM) |  |
|**os** | [**Os**](Os.md) |  |  |
|**policyMode** | [**PolicyModeEnum**](#PolicyModeEnum) | The policy mode for the node. Can only be specified when status&#x3D;accepted. If not specified, the default (global) mode will be used |  [optional] |
|**policyServerId** | **String** | The policy server ID for that node. By default, \&quot;root\&quot; |  [optional] |
|**properties** | [**List&lt;NodeAddInnerPropertiesInner&gt;**](NodeAddInnerPropertiesInner.md) | Node properties (either set by user or filled by third party sources) |  |
|**state** | [**StateEnum**](#StateEnum) | Node lifecycle state. Can only be specified when status&#x3D;accepted. If not specified, enable is used |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Target status of the node |  |
|**timezone** | [**Timezone**](Timezone.md) |  |  [optional] |



## Enum: MachineTypeEnum

| Name | Value |
|---- | -----|
| VMWARE | &quot;vmware&quot; |
| PHYSICAL | &quot;physical&quot; |
| VM | &quot;vm&quot; |
| SOLARISZONE | &quot;solariszone&quot; |
| QEMU | &quot;qemu&quot; |
| XEN | &quot;xen&quot; |
| AIXLPAR | &quot;aixlpar&quot; |
| HYPERV | &quot;hyperv&quot; |
| BSDJAIL | &quot;bsdjail&quot; |



## Enum: PolicyModeEnum

| Name | Value |
|---- | -----|
| ENFORCE | &quot;enforce&quot; |
| AUDIT | &quot;audit&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;enabled&quot; |
| IGNORED | &quot;ignored&quot; |
| EMPTY_POLICIES | &quot;empty-policies&quot; |
| INITIALIZING | &quot;initializing&quot; |
| PREPARING_EOL | &quot;preparing-eol&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ACCEPTED | &quot;accepted&quot; |
| PENDING | &quot;pending&quot; |



