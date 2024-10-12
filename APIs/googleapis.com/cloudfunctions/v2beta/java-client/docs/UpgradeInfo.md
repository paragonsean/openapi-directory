

# UpgradeInfo

Information related to: * A function's eligibility for 1st Gen to 2nd Gen migration * Current state of migration for function undergoing migration.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**buildConfig** | [**BuildConfig**](BuildConfig.md) |  |  [optional] |
|**eventTrigger** | [**EventTrigger**](EventTrigger.md) |  |  [optional] |
|**serviceConfig** | [**ServiceConfig**](ServiceConfig.md) |  |  [optional] |
|**upgradeState** | [**UpgradeStateEnum**](#UpgradeStateEnum) | UpgradeState of the function |  [optional] |



## Enum: UpgradeStateEnum

| Name | Value |
|---- | -----|
| UPGRADE_STATE_UNSPECIFIED | &quot;UPGRADE_STATE_UNSPECIFIED&quot; |
| ELIGIBLE_FOR_2_ND_GEN_UPGRADE | &quot;ELIGIBLE_FOR_2ND_GEN_UPGRADE&quot; |
| UPGRADE_OPERATION_IN_PROGRESS | &quot;UPGRADE_OPERATION_IN_PROGRESS&quot; |
| SETUP_FUNCTION_UPGRADE_CONFIG_SUCCESSFUL | &quot;SETUP_FUNCTION_UPGRADE_CONFIG_SUCCESSFUL&quot; |
| SETUP_FUNCTION_UPGRADE_CONFIG_ERROR | &quot;SETUP_FUNCTION_UPGRADE_CONFIG_ERROR&quot; |
| ABORT_FUNCTION_UPGRADE_ERROR | &quot;ABORT_FUNCTION_UPGRADE_ERROR&quot; |
| REDIRECT_FUNCTION_UPGRADE_TRAFFIC_SUCCESSFUL | &quot;REDIRECT_FUNCTION_UPGRADE_TRAFFIC_SUCCESSFUL&quot; |
| REDIRECT_FUNCTION_UPGRADE_TRAFFIC_ERROR | &quot;REDIRECT_FUNCTION_UPGRADE_TRAFFIC_ERROR&quot; |
| ROLLBACK_FUNCTION_UPGRADE_TRAFFIC_ERROR | &quot;ROLLBACK_FUNCTION_UPGRADE_TRAFFIC_ERROR&quot; |
| COMMIT_FUNCTION_UPGRADE_ERROR | &quot;COMMIT_FUNCTION_UPGRADE_ERROR&quot; |



