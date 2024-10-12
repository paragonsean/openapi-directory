# SiteRecoveryManagementClient.CreateRecoveryPlanInputProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failoverDeploymentModel** | **String** | The failover deployment model. | [optional] 
**groups** | [**[RecoveryPlanGroup]**](RecoveryPlanGroup.md) | The recovery plan groups. | 
**primaryFabricId** | **String** | The primary fabric Id. | 
**recoveryFabricId** | **String** | The recovery fabric Id. | 



## Enum: FailoverDeploymentModelEnum


* `NotApplicable` (value: `"NotApplicable"`)

* `Classic` (value: `"Classic"`)

* `ResourceManager` (value: `"ResourceManager"`)




