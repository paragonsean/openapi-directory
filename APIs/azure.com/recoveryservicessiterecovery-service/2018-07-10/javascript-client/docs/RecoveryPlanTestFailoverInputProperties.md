# SiteRecoveryManagementClient.RecoveryPlanTestFailoverInputProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failoverDirection** | **String** | The failover direction. | 
**networkId** | **String** | The Id of the network to be used for test failover. | [optional] 
**networkType** | **String** | The network type to be used for test failover. | 
**providerSpecificDetails** | [**[RecoveryPlanProviderSpecificFailoverInput]**](RecoveryPlanProviderSpecificFailoverInput.md) | The provider specific properties. | [optional] 
**skipTestFailoverCleanup** | **String** | A value indicating whether the test failover cleanup is to be skipped. | [optional] 



## Enum: FailoverDirectionEnum


* `PrimaryToRecovery` (value: `"PrimaryToRecovery"`)

* `RecoveryToPrimary` (value: `"RecoveryToPrimary"`)




