

# RollingUpgradeRunningStatus

Information about the current running state of the overall upgrade.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Code indicating the current status of the upgrade. |  [optional] [readonly] |
|**lastAction** | [**LastActionEnum**](#LastActionEnum) | The last action performed on the rolling upgrade. |  [optional] [readonly] |
|**lastActionTime** | **OffsetDateTime** | Last action time of the upgrade. |  [optional] [readonly] |
|**startTime** | **OffsetDateTime** | Start time of the upgrade. |  [optional] [readonly] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| ROLLING_FORWARD | &quot;RollingForward&quot; |
| CANCELLED | &quot;Cancelled&quot; |
| COMPLETED | &quot;Completed&quot; |
| FAULTED | &quot;Faulted&quot; |



## Enum: LastActionEnum

| Name | Value |
|---- | -----|
| START | &quot;Start&quot; |
| CANCEL | &quot;Cancel&quot; |



