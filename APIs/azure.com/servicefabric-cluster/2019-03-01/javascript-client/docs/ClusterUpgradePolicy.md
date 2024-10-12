# ServiceFabricManagementClient.ClusterUpgradePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deltaHealthPolicy** | [**ClusterUpgradeDeltaHealthPolicy**](ClusterUpgradeDeltaHealthPolicy.md) |  | [optional] 
**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). | [optional] 
**healthCheckRetryTimeout** | **String** | The amount of time to retry health evaluation when the application or cluster is unhealthy before the upgrade rolls back. The timeout can be in either hh:mm:ss or in d.hh:mm:ss.ms format. | 
**healthCheckStableDuration** | **String** | The amount of time that the application or cluster must remain healthy before the upgrade proceeds to the next upgrade domain. The duration can be in either hh:mm:ss or in d.hh:mm:ss.ms format. | 
**healthCheckWaitDuration** | **String** | The length of time to wait after completing an upgrade domain before performing health checks. The duration can be in either hh:mm:ss or in d.hh:mm:ss.ms format. | 
**healthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md) |  | 
**upgradeDomainTimeout** | **String** | The amount of time each upgrade domain has to complete before the upgrade rolls back. The timeout can be in either hh:mm:ss or in d.hh:mm:ss.ms format. | 
**upgradeReplicaSetCheckTimeout** | **String** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. The timeout can be in either hh:mm:ss or in d.hh:mm:ss.ms format. | 
**upgradeTimeout** | **String** | The amount of time the overall upgrade has to complete before the upgrade rolls back. The timeout can be in either hh:mm:ss or in d.hh:mm:ss.ms format. | 


