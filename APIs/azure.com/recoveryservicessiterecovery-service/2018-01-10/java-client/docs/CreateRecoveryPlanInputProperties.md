

# CreateRecoveryPlanInputProperties

Recovery plan creation properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failoverDeploymentModel** | [**FailoverDeploymentModelEnum**](#FailoverDeploymentModelEnum) | The failover deployment model. |  [optional] |
|**groups** | [**List&lt;RecoveryPlanGroup&gt;**](RecoveryPlanGroup.md) | The recovery plan groups. |  |
|**primaryFabricId** | **String** | The primary fabric Id. |  |
|**recoveryFabricId** | **String** | The recovery fabric Id. |  |



## Enum: FailoverDeploymentModelEnum

| Name | Value |
|---- | -----|
| NOT_APPLICABLE | &quot;NotApplicable&quot; |
| CLASSIC | &quot;Classic&quot; |
| RESOURCE_MANAGER | &quot;ResourceManager&quot; |



