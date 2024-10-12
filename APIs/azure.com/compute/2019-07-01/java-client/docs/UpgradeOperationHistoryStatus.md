

# UpgradeOperationHistoryStatus

Information about the current running state of the overall upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Code indicating the current status of the upgrade. |  [optional] [readonly] |
|**endTime** | **OffsetDateTime** | End time of the upgrade. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | Start time of the upgrade. |  [optional] [readonly] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| ROLLING_FORWARD | &quot;RollingForward&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAULTED | &quot;Faulted&quot; |



