# KubernetesEngineApi.OpportunisticMaintenanceStrategy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintenanceAvailabilityWindow** | **String** | The window of time that opportunistic maintenance can run. Example: A setting of 14 days implies that opportunistic maintenance can only be ran in the 2 weeks leading up to the scheduled maintenance date. Setting 28 days allows opportunistic maintenance to run at any time in the scheduled maintenance window (all &#x60;PERIODIC&#x60; maintenance is set 28 days in advance). | [optional] 
**minNodesPerPool** | **String** | The minimum nodes required to be available in a pool. Blocks maintenance if it would cause the number of running nodes to dip below this value. | [optional] 
**nodeIdleTimeWindow** | **String** | The amount of time that a node can remain idle (no customer owned workloads running), before triggering maintenance. | [optional] 


