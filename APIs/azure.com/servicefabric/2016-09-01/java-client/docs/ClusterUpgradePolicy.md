

# ClusterUpgradePolicy

Cluster upgrade policy

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deltaHealthPolicy** | [**ClusterUpgradeDeltaHealthPolicy**](ClusterUpgradeDeltaHealthPolicy.md) |  |  [optional] |
|**forceRestart** | **Boolean** | Force node to restart or not |  [optional] |
|**healthCheckRetryTimeout** | **String** | The length of time that health checks can fail continuously,it represents .Net TimeSpan |  |
|**healthCheckStableDuration** | **String** | The length of time that health checks must pass continuously,it represents .Net TimeSpan |  |
|**healthCheckWaitDuration** | **String** | The length of time to wait after completing an upgrade domain before performing health checks, it represents .Net TimeSpan |  |
|**healthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md) |  |  |
|**overrideUserUpgradePolicy** | **Boolean** | Use the user defined upgrade policy or not |  [optional] |
|**upgradeDomainTimeout** | **String** | The timeout for any upgrade domain,it represents .Net TimeSpan |  |
|**upgradeReplicaSetCheckTimeout** | **String** | Timeout for replica set upgrade to complete,it represents .Net TimeSpan |  |
|**upgradeTimeout** | **String** | The upgrade timeout,it represents .Net TimeSpan |  |



