

# CostThresholdProperties

Properties of a cost threshold item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayOnChart** | [**DisplayOnChartEnum**](#DisplayOnChartEnum) | Indicates whether this threshold will be displayed on cost charts. |  [optional] |
|**notificationSent** | **String** | Indicates the datetime when notifications were last sent for this threshold. |  [optional] |
|**percentageThreshold** | [**PercentageCostThresholdProperties**](PercentageCostThresholdProperties.md) |  |  [optional] |
|**sendNotificationWhenExceeded** | [**SendNotificationWhenExceededEnum**](#SendNotificationWhenExceededEnum) | Indicates whether notifications will be sent when this threshold is exceeded. |  [optional] |
|**thresholdId** | **String** | The ID of the cost threshold item. |  [optional] |



## Enum: DisplayOnChartEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



## Enum: SendNotificationWhenExceededEnum

| Name | Value |
|---- | -----|
| ENABLED | &quot;Enabled&quot; |
| DISABLED | &quot;Disabled&quot; |



