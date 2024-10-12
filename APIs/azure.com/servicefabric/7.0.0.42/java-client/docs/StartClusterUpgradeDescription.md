

# StartClusterUpgradeDescription

Describes the parameters for starting a cluster upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationHealthPolicyMap** | [**ApplicationHealthPolicies**](ApplicationHealthPolicies.md) |  |  [optional] |
|**clusterHealthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md) |  |  [optional] |
|**clusterUpgradeHealthPolicy** | [**ClusterUpgradeHealthPolicyObject**](ClusterUpgradeHealthPolicyObject.md) |  |  [optional] |
|**codeVersion** | **String** | The cluster code version. |  [optional] |
|**configVersion** | **String** | The cluster configuration version. |  [optional] |
|**enableDeltaHealthEvaluation** | **Boolean** | When true, enables delta health evaluation rather than absolute health evaluation after completion of each upgrade domain. |  [optional] |
|**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). |  [optional] |
|**instanceCloseDelayDurationInSeconds** | **Long** | Duration in seconds, to wait before a stateless instance is closed, to allow the active requests to drain gracefully. This would be effective when the instance is closing during the application/cluster upgrade, only for those instances which have a non-zero delay duration configured in the service description. See InstanceCloseDelayDurationSeconds property in $ref: \&quot;#/definitions/StatelessServiceDescription.yaml\&quot; for details. Note, the default value of InstanceCloseDelayDurationInSeconds is 4294967295, which indicates that the behavior will entirely depend on the delay configured in the stateless service description. |  [optional] |
|**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  |  [optional] |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**sortOrder** | **UpgradeSortOrder** |  |  [optional] |
|**upgradeKind** | **UpgradeKind** |  |  [optional] |
|**upgradeReplicaSetCheckTimeoutInSeconds** | **Long** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). |  [optional] |



