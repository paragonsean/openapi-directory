

# TargetFrequency

Setting that controls the average number of times the ads will show to the same person over a certain period of time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**targetCount** | **String** | The target number of times, on average, the ads will be shown to the same person in the timespan dictated by time_unit and time_unit_count. |  [optional] |
|**timeUnit** | [**TimeUnitEnum**](#TimeUnitEnum) | The unit of time in which the target frequency will be applied. The following time unit is applicable: * &#x60;TIME_UNIT_WEEKS&#x60; |  [optional] |
|**timeUnitCount** | **Integer** | The number of time_unit the target frequency will last. The following restrictions apply based on the value of time_unit: * &#x60;TIME_UNIT_WEEKS&#x60; - must be 1 |  [optional] |



## Enum: TimeUnitEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;TIME_UNIT_UNSPECIFIED&quot; |
| LIFETIME | &quot;TIME_UNIT_LIFETIME&quot; |
| MONTHS | &quot;TIME_UNIT_MONTHS&quot; |
| WEEKS | &quot;TIME_UNIT_WEEKS&quot; |
| DAYS | &quot;TIME_UNIT_DAYS&quot; |
| HOURS | &quot;TIME_UNIT_HOURS&quot; |
| MINUTES | &quot;TIME_UNIT_MINUTES&quot; |



