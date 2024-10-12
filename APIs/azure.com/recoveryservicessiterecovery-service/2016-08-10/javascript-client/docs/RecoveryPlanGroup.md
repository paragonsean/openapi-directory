# SiteRecoveryManagementClient.RecoveryPlanGroup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endGroupActions** | [**[RecoveryPlanAction]**](RecoveryPlanAction.md) | The end group actions. | [optional] 
**groupType** | **String** | The group type. | 
**replicationProtectedItems** | [**[RecoveryPlanProtectedItem]**](RecoveryPlanProtectedItem.md) | The list of protected items. | [optional] 
**startGroupActions** | [**[RecoveryPlanAction]**](RecoveryPlanAction.md) | The start group actions. | [optional] 



## Enum: GroupTypeEnum


* `Shutdown` (value: `"Shutdown"`)

* `Boot` (value: `"Boot"`)

* `Failover` (value: `"Failover"`)




