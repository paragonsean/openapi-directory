# CloudDeployApi.SkaffoldSupportedCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintenanceModeTime** | **String** | The time at which this release&#39;s version of Skaffold will enter maintenance mode. | [optional] 
**skaffoldSupportState** | **String** | The Skaffold support state for this release&#39;s version of Skaffold. | [optional] 
**status** | **Boolean** | True if the version of Skaffold used by this release is supported. | [optional] 
**supportExpirationTime** | **String** | The time at which this release&#39;s version of Skaffold will no longer be supported. | [optional] 



## Enum: SkaffoldSupportStateEnum


* `UNSPECIFIED` (value: `"SKAFFOLD_SUPPORT_STATE_UNSPECIFIED"`)

* `SUPPORTED` (value: `"SKAFFOLD_SUPPORT_STATE_SUPPORTED"`)

* `MAINTENANCE_MODE` (value: `"SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE"`)

* `UNSUPPORTED` (value: `"SKAFFOLD_SUPPORT_STATE_UNSUPPORTED"`)




