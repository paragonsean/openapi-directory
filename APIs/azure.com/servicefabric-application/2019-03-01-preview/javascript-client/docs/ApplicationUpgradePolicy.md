# ServiceFabricManagementClient.ApplicationUpgradePolicy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**applicationHealthPolicy** | [**ArmApplicationHealthPolicy**](ArmApplicationHealthPolicy.md) |  | [optional] 
**forceRestart** | **Boolean** | If true, then processes are forcefully restarted during upgrade even when the code version has not changed (the upgrade only changes configuration or data). | [optional] [default to false]
**rollingUpgradeMonitoringPolicy** | [**ArmRollingUpgradeMonitoringPolicy**](ArmRollingUpgradeMonitoringPolicy.md) |  | [optional] 
**upgradeReplicaSetCheckTimeout** | **String** | The maximum amount of time to block processing of an upgrade domain and prevent loss of availability when there are unexpected issues. When this timeout expires, processing of the upgrade domain will proceed regardless of availability loss issues. The timeout is reset at the start of each upgrade domain. Valid values are between 0 and 42949672925 inclusive. (unsigned 32-bit integer). | [optional] 


