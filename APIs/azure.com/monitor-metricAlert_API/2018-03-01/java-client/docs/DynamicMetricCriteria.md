

# DynamicMetricCriteria

Criterion for dynamic threshold.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**alertSensitivity** | [**AlertSensitivityEnum**](#AlertSensitivityEnum) | The extent of deviation required to trigger an alert. This will affect how tight the threshold is to the metric series pattern. |  |
|**failingPeriods** | [**DynamicThresholdFailingPeriods**](DynamicThresholdFailingPeriods.md) |  |  |
|**ignoreDataBefore** | **OffsetDateTime** | Use this option to set the date from which to start learning the metric historical data and calculate the dynamic thresholds (in ISO8601 format) |  [optional] |
|**operator** | [**OperatorEnum**](#OperatorEnum) | The operator used to compare the metric value against the threshold. |  |



## Enum: AlertSensitivityEnum

| Name | Value |
|---- | -----|
| LOW | &quot;Low&quot; |
| MEDIUM | &quot;Medium&quot; |
| HIGH | &quot;High&quot; |



## Enum: OperatorEnum

| Name | Value |
|---- | -----|
| GREATER_THAN | &quot;GreaterThan&quot; |
| LESS_THAN | &quot;LessThan&quot; |
| GREATER_OR_LESS_THAN | &quot;GreaterOrLessThan&quot; |



