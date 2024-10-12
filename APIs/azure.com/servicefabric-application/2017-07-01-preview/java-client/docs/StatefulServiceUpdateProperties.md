

# StatefulServiceUpdateProperties

The properties of a stateful service resource for patch operations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**minReplicaSetSize** | **Integer** | The minimum replica set size as a number. |  [optional] |
|**quorumLossWaitDuration** | **OffsetDateTime** | The maximum duration for which a partition is allowed to be in a state of quorum loss, represented in ISO 8601 format (hh:mm:ss.s). |  [optional] |
|**replicaRestartWaitDuration** | **OffsetDateTime** | The duration between when a replica goes down and when a new replica is created, represented in ISO 8601 format (hh:mm:ss.s). |  [optional] |
|**standByReplicaKeepDuration** | **OffsetDateTime** | The definition on how long StandBy replicas should be maintained before being removed, represented in ISO 8601 format (hh:mm:ss.s). |  [optional] |
|**targetReplicaSetSize** | **Integer** | The target replica set size as a number. |  [optional] |
|**serviceKind** | **ServiceKind** |  |  |
|**correlationScheme** | [**List&lt;ServiceCorrelationDescription&gt;**](ServiceCorrelationDescription.md) | A list that describes the correlation of the service with other services. |  [optional] |
|**defaultMoveCost** | **MoveCost** |  |  [optional] |
|**placementConstraints** | **String** | The placement constraints as a string. Placement constraints are boolean expressions on node properties and allow for restricting a service to particular nodes based on the service requirements. For example, to place a service on nodes where NodeType is blue specify the following: \&quot;NodeColor &#x3D;&#x3D; blue)\&quot;. |  [optional] |
|**serviceLoadMetrics** | [**List&lt;ServiceLoadMetricDescription&gt;**](ServiceLoadMetricDescription.md) | The service load metrics is given as an array of ServiceLoadMetricDescription objects. |  [optional] |
|**servicePlacementPolicies** | [**List&lt;ServicePlacementPolicyDescription&gt;**](ServicePlacementPolicyDescription.md) | A list that describes the correlation of the service with other services. |  [optional] |



