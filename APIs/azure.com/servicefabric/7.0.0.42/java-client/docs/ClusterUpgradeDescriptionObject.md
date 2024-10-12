

# ClusterUpgradeDescriptionObject

Represents a ServiceFabric cluster upgrade

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**applicationHealthPolicyMap** | [**List&lt;ApplicationHealthPolicyMapItem&gt;**](ApplicationHealthPolicyMapItem.md) | Defines a map that contains specific application health policies for different applications. Each entry specifies as key the application name and as value an ApplicationHealthPolicy used to evaluate the application health. If an application is not specified in the map, the application health evaluation uses the ApplicationHealthPolicy found in its application manifest or the default application health policy (if no health policy is defined in the manifest). The map is empty by default. |  [optional] |
|**clusterHealthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md) |  |  [optional] |
|**clusterUpgradeHealthPolicy** | [**ClusterUpgradeHealthPolicyObject**](ClusterUpgradeHealthPolicyObject.md) |  |  [optional] |
|**codeVersion** | **String** | The ServiceFabric code version of the cluster. |  [optional] |
|**configVersion** | **String** | The cluster configuration version (specified in the cluster manifest). |  [optional] |
|**enableDeltaHealthEvaluation** | **Boolean** | When true, enables delta health evaluation rather than absolute health evaluation after completion of each upgrade domain. |  [optional] |
|**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). |  [optional] |
|**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  |  [optional] |
|**rollingUpgradeMode** | **UpgradeMode** |  |  [optional] |
|**sortOrder** | **UpgradeSortOrder** |  |  [optional] |
|**upgradeKind** | **UpgradeKind** |  |  [optional] |
|**upgradeReplicaSetCheckTimeoutInSeconds** | **Long** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). |  [optional] |



