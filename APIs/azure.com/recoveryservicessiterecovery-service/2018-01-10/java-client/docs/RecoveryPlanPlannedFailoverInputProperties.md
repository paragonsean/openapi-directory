

# RecoveryPlanPlannedFailoverInputProperties

Recovery plan planned failover input properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failoverDirection** | [**FailoverDirectionEnum**](#FailoverDirectionEnum) | The failover direction. |  |
|**providerSpecificDetails** | [**List&lt;RecoveryPlanProviderSpecificFailoverInput&gt;**](RecoveryPlanProviderSpecificFailoverInput.md) | The provider specific properties. |  [optional] |



## Enum: FailoverDirectionEnum

| Name | Value |
|---- | -----|
| PRIMARY_TO_RECOVERY | &quot;PrimaryToRecovery&quot; |
| RECOVERY_TO_PRIMARY | &quot;RecoveryToPrimary&quot; |



