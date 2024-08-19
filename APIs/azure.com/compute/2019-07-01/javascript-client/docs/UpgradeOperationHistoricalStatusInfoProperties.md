# ComputeManagementClient.UpgradeOperationHistoricalStatusInfoProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**ApiError**](ApiError.md) |  | [optional] 
**progress** | [**RollingUpgradeProgressInfo**](RollingUpgradeProgressInfo.md) |  | [optional] 
**rollbackInfo** | [**RollbackStatusInfo**](RollbackStatusInfo.md) |  | [optional] 
**runningStatus** | [**UpgradeOperationHistoryStatus**](UpgradeOperationHistoryStatus.md) |  | [optional] 
**startedBy** | **String** | Invoker of the Upgrade Operation | [optional] [readonly] 
**targetImageReference** | [**ImageReference**](ImageReference.md) |  | [optional] 



## Enum: StartedByEnum


* `Unknown` (value: `"Unknown"`)

* `User` (value: `"User"`)

* `Platform` (value: `"Platform"`)




