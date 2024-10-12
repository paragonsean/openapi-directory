

# TargetCostProperties

Properties of a cost target.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**costThresholds** | [**List&lt;CostThresholdProperties&gt;**](CostThresholdProperties.md) | Cost thresholds. |  [optional] |
|**cycleEndDateTime** | **OffsetDateTime** | Reporting cycle end date. |  [optional] |
|**cycleStartDateTime** | **OffsetDateTime** | Reporting cycle start date. |  [optional] |
|**cycleType** | [**CycleTypeEnum**](#CycleTypeEnum) | Reporting cycle type. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Target cost status |  [optional] |
|**target** | **Integer** | Lab target cost |  [optional] |



## Enum: CycleTypeEnum

| Name | Value |
|---- | -----|
| CALENDAR_MONTH | &quot;CalendarMonth&quot; |
| CUSTOM | &quot;Custom&quot; |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



