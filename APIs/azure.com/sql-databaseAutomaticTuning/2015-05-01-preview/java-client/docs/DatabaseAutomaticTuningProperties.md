

# DatabaseAutomaticTuningProperties

Database-level Automatic Tuning properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**actualState** | [**ActualStateEnum**](#ActualStateEnum) | Automatic tuning actual state. |  [optional] [readonly] |
|**desiredState** | [**DesiredStateEnum**](#DesiredStateEnum) | Automatic tuning desired state. |  [optional] |
|**options** | [**Map&lt;String, AutomaticTuningOptions&gt;**](AutomaticTuningOptions.md) | Automatic tuning options definition. |  [optional] |



## Enum: ActualStateEnum

| Name | Value |
|---- | -----|
| INHERIT | &quot;Inherit&quot; |
| CUSTOM | &quot;Custom&quot; |
| AUTO | &quot;Auto&quot; |
| UNSPECIFIED | &quot;Unspecified&quot; |



## Enum: DesiredStateEnum

| Name | Value |
|---- | -----|
| INHERIT | &quot;Inherit&quot; |
| CUSTOM | &quot;Custom&quot; |
| AUTO | &quot;Auto&quot; |
| UNSPECIFIED | &quot;Unspecified&quot; |



