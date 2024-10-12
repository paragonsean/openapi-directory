

# AmlComputeAllOfProperties

AML Compute properties

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allocationState** | [**AllocationStateEnum**](#AllocationStateEnum) | Allocation state of the compute. Possible values are: steady - Indicates that the compute is not resizing. There are no changes to the number of compute nodes in the compute in progress. A compute enters this state when it is created and when no operations are being performed on the compute to change the number of compute nodes. resizing - Indicates that the compute is resizing; that is, compute nodes are being added to or removed from the compute. |  [optional] [readonly] |
|**allocationStateTransitionTime** | **OffsetDateTime** | The time at which the compute entered its current allocation state. |  [optional] [readonly] |
|**currentNodeCount** | **Integer** | The number of compute nodes currently assigned to the compute. |  [optional] [readonly] |
|**errors** | [**List&lt;MachineLearningServiceError&gt;**](MachineLearningServiceError.md) | Collection of errors encountered by various compute nodes during node setup. |  [optional] [readonly] |
|**nodeStateCounts** | [**NodeStateCounts**](NodeStateCounts.md) |  |  [optional] |
|**remoteLoginPortPublicAccess** | [**RemoteLoginPortPublicAccessEnum**](#RemoteLoginPortPublicAccessEnum) | State of the public SSH port. Possible values are: Disabled - Indicates that the public ssh port is closed on all nodes of the cluster. Enabled - Indicates that the public ssh port is open on all nodes of the cluster. NotSpecified - Indicates that the public ssh port is closed on all nodes of the cluster if VNet is defined, else is open all public nodes. It can be default only during cluster creation time, after creation it will be either enabled or disabled. |  [optional] |
|**scaleSettings** | [**ScaleSettings**](ScaleSettings.md) |  |  [optional] |
|**subnet** | [**ResourceId**](ResourceId.md) |  |  [optional] |
|**targetNodeCount** | **Integer** | The target number of compute nodes for the compute. If the allocationState is resizing, this property denotes the target node count for the ongoing resize operation. If the allocationState is steady, this property denotes the target node count for the previous resize operation. |  [optional] [readonly] |
|**userAccountCredentials** | [**UserAccountCredentials**](UserAccountCredentials.md) |  |  [optional] |
|**vmPriority** | [**VmPriorityEnum**](#VmPriorityEnum) | Virtual Machine priority |  [optional] |
|**vmSize** | **String** | Virtual Machine Size |  [optional] |



## Enum: AllocationStateEnum

| Name | Value |
|---- | -----|
| STEADY | &quot;Steady&quot; |
| RESIZING | &quot;Resizing&quot; |



## Enum: RemoteLoginPortPublicAccessEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |
| NOT_SPECIFIED | &quot;NotSpecified&quot; |



## Enum: VmPriorityEnum

| Name | Value |
|---- | -----|
| DEDICATED | &quot;Dedicated&quot; |
| LOW_PRIORITY | &quot;LowPriority&quot; |



