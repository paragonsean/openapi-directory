

# RecoveryPlanTestFailoverInputProperties

Recovery plan test failover input properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failoverDirection** | [**FailoverDirectionEnum**](#FailoverDirectionEnum) | The failover direction. |  |
|**networkId** | **String** | The Id of the network to be used for test failover. |  [optional] |
|**networkType** | **String** | The network type to be used for test failover. |  |
|**providerSpecificDetails** | [**List&lt;RecoveryPlanProviderSpecificFailoverInput&gt;**](RecoveryPlanProviderSpecificFailoverInput.md) | The provider specific properties. |  [optional] |
|**skipTestFailoverCleanup** | **String** | A value indicating whether the test failover cleanup is to be skipped. |  [optional] |



## Enum: FailoverDirectionEnum

| Name | Value |
|---- | -----|
| PRIMARY_TO_RECOVERY | &quot;PrimaryToRecovery&quot; |
| RECOVERY_TO_PRIMARY | &quot;RecoveryToPrimary&quot; |



