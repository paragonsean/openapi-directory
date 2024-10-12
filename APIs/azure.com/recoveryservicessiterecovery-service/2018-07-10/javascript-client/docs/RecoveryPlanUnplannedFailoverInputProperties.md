# SiteRecoveryManagementClient.RecoveryPlanUnplannedFailoverInputProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failoverDirection** | **String** | The failover direction. | 
**providerSpecificDetails** | [**[RecoveryPlanProviderSpecificFailoverInput]**](RecoveryPlanProviderSpecificFailoverInput.md) | The provider specific properties. | [optional] 
**sourceSiteOperations** | **String** | A value indicating whether source site operations are required. | 



## Enum: FailoverDirectionEnum


* `PrimaryToRecovery` (value: `"PrimaryToRecovery"`)

* `RecoveryToPrimary` (value: `"RecoveryToPrimary"`)





## Enum: SourceSiteOperationsEnum


* `Required` (value: `"Required"`)

* `NotRequired` (value: `"NotRequired"`)




