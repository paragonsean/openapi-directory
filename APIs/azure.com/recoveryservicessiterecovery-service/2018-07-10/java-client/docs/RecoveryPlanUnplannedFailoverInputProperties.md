

# RecoveryPlanUnplannedFailoverInputProperties

Recovery plan unplanned failover input properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failoverDirection** | [**FailoverDirectionEnum**](#FailoverDirectionEnum) | The failover direction. |  |
|**providerSpecificDetails** | [**List&lt;RecoveryPlanProviderSpecificFailoverInput&gt;**](RecoveryPlanProviderSpecificFailoverInput.md) | The provider specific properties. |  [optional] |
|**sourceSiteOperations** | [**SourceSiteOperationsEnum**](#SourceSiteOperationsEnum) | A value indicating whether source site operations are required. |  |



## Enum: FailoverDirectionEnum

| Name | Value |
|---- | -----|
| PRIMARY_TO_RECOVERY | &quot;PrimaryToRecovery&quot; |
| RECOVERY_TO_PRIMARY | &quot;RecoveryToPrimary&quot; |



## Enum: SourceSiteOperationsEnum

| Name | Value |
|---- | -----|
| REQUIRED | &quot;Required&quot; |
| NOT_REQUIRED | &quot;NotRequired&quot; |



