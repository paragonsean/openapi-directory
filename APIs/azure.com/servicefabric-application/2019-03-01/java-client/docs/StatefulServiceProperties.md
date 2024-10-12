

# StatefulServiceProperties

The properties of a stateful service resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**hasPersistedState** | **Boolean** | A flag indicating whether this is a persistent service which stores states on the local disk. If it is then the value of this property is true, if not it is false. |  [optional] |
|**minReplicaSetSize** | **Integer** | The minimum replica set size as a number. |  [optional] |
|**quorumLossWaitDuration** | **OffsetDateTime** | The maximum duration for which a partition is allowed to be in a state of quorum loss, represented in ISO 8601 format (hh:mm:ss.s). |  [optional] |
|**replicaRestartWaitDuration** | **OffsetDateTime** | The duration between when a replica goes down and when a new replica is created, represented in ISO 8601 format (hh:mm:ss.s). |  [optional] |
|**standByReplicaKeepDuration** | **OffsetDateTime** | The definition on how long StandBy replicas should be maintained before being removed, represented in ISO 8601 format (hh:mm:ss.s). |  [optional] |
|**targetReplicaSetSize** | **Integer** | The target replica set size as a number. |  [optional] |
|**partitionDescription** | [**PartitionSchemeDescription**](PartitionSchemeDescription.md) |  |  [optional] |
|**provisioningState** | **String** | The current deployment or provisioning state, which only appears in the response |  [optional] [readonly] |
|**serviceKind** | **ServiceKind** |  |  |
|**servicePackageActivationMode** | [**ServicePackageActivationModeEnum**](#ServicePackageActivationModeEnum) | The activation Mode of the service package |  [optional] |
|**serviceTypeName** | **String** | The name of the service type |  [optional] |
|**correlationScheme** | [**List&lt;ServiceCorrelationDescription&gt;**](ServiceCorrelationDescription.md) | A list that describes the correlation of the service with other services. |  [optional] |
|**defaultMoveCost** | **MoveCost** |  |  [optional] |
|**placementConstraints** | **String** | The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: \&quot;NodeColor &#x3D;&#x3D; blue)\&quot;. |  [optional] |
|**serviceLoadMetrics** | [**List&lt;ServiceLoadMetricDescription&gt;**](ServiceLoadMetricDescription.md) | The service load metrics is given as an array of ServiceLoadMetricDescription objects. |  [optional] |
|**servicePlacementPolicies** | [**List&lt;ServicePlacementPolicyDescription&gt;**](ServicePlacementPolicyDescription.md) | A list that describes the correlation of the service with other services. |  [optional] |



## Enum: ServicePackageActivationModeEnum

| Name | Value |
|---- | -----|
| SHARED_PROCESS | &quot;SharedProcess&quot; |
| EXCLUSIVE_PROCESS | &quot;ExclusiveProcess&quot; |



