

# UpgradeOperationHistoricalStatusInfoProperties

Describes each OS upgrade on the Virtual Machine Scale Set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ApiError**](ApiError.md) |  |  [optional] |
|**progress** | [**RollingUpgradeProgressInfo**](RollingUpgradeProgressInfo.md) |  |  [optional] |
|**rollbackInfo** | [**RollbackStatusInfo**](RollbackStatusInfo.md) |  |  [optional] |
|**runningStatus** | [**UpgradeOperationHistoryStatus**](UpgradeOperationHistoryStatus.md) |  |  [optional] |
|**startedBy** | [**StartedByEnum**](#StartedByEnum) | Invoker of the Upgrade Operation |  [optional] [readonly] |
|**targetImageReference** | [**ImageReference**](ImageReference.md) |  |  [optional] |



## Enum: StartedByEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;Unknown&quot; |
| USER | &quot;User&quot; |
| PLATFORM | &quot;Platform&quot; |



