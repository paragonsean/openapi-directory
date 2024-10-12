

# SuppressionConfig

Suppression logic for a given action rule

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**recurrenceType** | [**RecurrenceTypeEnum**](#RecurrenceTypeEnum) | Specifies when the suppression should be applied |  |
|**schedule** | [**SuppressionSchedule**](SuppressionSchedule.md) |  |  [optional] |



## Enum: RecurrenceTypeEnum

| Name | Value |
|---- | -----|
| ALWAYS | &quot;Always&quot; |
| ONCE | &quot;Once&quot; |
| DAILY | &quot;Daily&quot; |
| WEEKLY | &quot;Weekly&quot; |
| MONTHLY | &quot;Monthly&quot; |



