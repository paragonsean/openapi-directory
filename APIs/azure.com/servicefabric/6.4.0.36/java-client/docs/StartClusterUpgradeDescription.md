

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
|**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  |  [optional] |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**upgradeKind** | **UpgradeKind** |  |  [optional] |
|**upgradeReplicaSetCheckTimeoutInSeconds** | **Long** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). |  [optional] |



