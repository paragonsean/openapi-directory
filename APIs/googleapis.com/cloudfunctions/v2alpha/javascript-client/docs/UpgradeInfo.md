# CloudFunctionsApi.UpgradeInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**buildConfig** | [**BuildConfig**](BuildConfig.md) |  | [optional] 
**eventTrigger** | [**EventTrigger**](EventTrigger.md) |  | [optional] 
**serviceConfig** | [**ServiceConfig**](ServiceConfig.md) |  | [optional] 
**upgradeState** | **String** | UpgradeState of the function | [optional] 



## Enum: UpgradeStateEnum


* `UPGRADE_STATE_UNSPECIFIED` (value: `"UPGRADE_STATE_UNSPECIFIED"`)

* `ELIGIBLE_FOR_2ND_GEN_UPGRADE` (value: `"ELIGIBLE_FOR_2ND_GEN_UPGRADE"`)

* `UPGRADE_OPERATION_IN_PROGRESS` (value: `"UPGRADE_OPERATION_IN_PROGRESS"`)

* `SETUP_FUNCTION_UPGRADE_CONFIG_SUCCESSFUL` (value: `"SETUP_FUNCTION_UPGRADE_CONFIG_SUCCESSFUL"`)

* `SETUP_FUNCTION_UPGRADE_CONFIG_ERROR` (value: `"SETUP_FUNCTION_UPGRADE_CONFIG_ERROR"`)

* `ABORT_FUNCTION_UPGRADE_ERROR` (value: `"ABORT_FUNCTION_UPGRADE_ERROR"`)

* `REDIRECT_FUNCTION_UPGRADE_TRAFFIC_SUCCESSFUL` (value: `"REDIRECT_FUNCTION_UPGRADE_TRAFFIC_SUCCESSFUL"`)

* `REDIRECT_FUNCTION_UPGRADE_TRAFFIC_ERROR` (value: `"REDIRECT_FUNCTION_UPGRADE_TRAFFIC_ERROR"`)

* `ROLLBACK_FUNCTION_UPGRADE_TRAFFIC_ERROR` (value: `"ROLLBACK_FUNCTION_UPGRADE_TRAFFIC_ERROR"`)

* `COMMIT_FUNCTION_UPGRADE_ERROR` (value: `"COMMIT_FUNCTION_UPGRADE_ERROR"`)




