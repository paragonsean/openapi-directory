

# SkaffoldSupportedCondition

SkaffoldSupportedCondition contains information about when support for the release's version of Skaffold ends.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maintenanceModeTime** | **String** | The time at which this release&#39;s version of Skaffold will enter maintenance mode. |  [optional] |
|**skaffoldSupportState** | [**SkaffoldSupportStateEnum**](#SkaffoldSupportStateEnum) | The Skaffold support state for this release&#39;s version of Skaffold. |  [optional] |
|**status** | **Boolean** | True if the version of Skaffold used by this release is supported. |  [optional] |
|**supportExpirationTime** | **String** | The time at which this release&#39;s version of Skaffold will no longer be supported. |  [optional] |



## Enum: SkaffoldSupportStateEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;SKAFFOLD_SUPPORT_STATE_UNSPECIFIED&quot; |
| SUPPORTED | &quot;SKAFFOLD_SUPPORT_STATE_SUPPORTED&quot; |
| MAINTENANCE_MODE | &quot;SKAFFOLD_SUPPORT_STATE_MAINTENANCE_MODE&quot; |
| UNSUPPORTED | &quot;SKAFFOLD_SUPPORT_STATE_UNSUPPORTED&quot; |



