

# RecoveryPlanGroup

Recovery plan group details.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endGroupActions** | [**List&lt;RecoveryPlanAction&gt;**](RecoveryPlanAction.md) | The end group actions. |  [optional] |
|**groupType** | [**GroupTypeEnum**](#GroupTypeEnum) | The group type. |  |
|**replicationProtectedItems** | [**List&lt;RecoveryPlanProtectedItem&gt;**](RecoveryPlanProtectedItem.md) | The list of protected items. |  [optional] |
|**startGroupActions** | [**List&lt;RecoveryPlanAction&gt;**](RecoveryPlanAction.md) | The start group actions. |  [optional] |



## Enum: GroupTypeEnum

| Name | Value |
|---- | -----|
| SHUTDOWN | &quot;Shutdown&quot; |
| BOOT | &quot;Boot&quot; |
| FAILOVER | &quot;Failover&quot; |



