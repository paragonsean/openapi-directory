# ServiceFabricClientApis.StartClusterUpgradeDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationHealthPolicyMap** | [**ApplicationHealthPolicies**](ApplicationHealthPolicies.md) |  | [optional] 
**clusterHealthPolicy** | [**ClusterHealthPolicy**](ClusterHealthPolicy.md) |  | [optional] 
**clusterUpgradeHealthPolicy** | [**ClusterUpgradeHealthPolicyObject**](ClusterUpgradeHealthPolicyObject.md) |  | [optional] 
**codeVersion** | **String** | The cluster code version. | [optional] 
**configVersion** | **String** | The cluster configuration version. | [optional] 
**enableDeltaHealthEvaluation** | **Boolean** | When true, enables delta health evaluation rather than absolute health evaluation after completion of each upgrade domain. | [optional] 
**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). | [optional] [default to false]
**monitoringPolicy** | [**MonitoringPolicyDescription**](MonitoringPolicyDescription.md) |  | [optional] 
**rollingUpgradeMode** | [**UpgradeMode**](UpgradeMode.md) |  | [optional] 
**upgradeKind** | [**UpgradeKind**](UpgradeKind.md) |  | [optional] 
**upgradeReplicaSetCheckTimeoutInSeconds** | **Number** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). | [optional] 


