

# FrequencyCap

Message contains details about publisher-set frequency caps of the delivery.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**maxImpressions** | **Integer** | The maximum number of impressions that can be served to a user within the specified time period. |  [optional] |
|**timeUnitType** | [**TimeUnitTypeEnum**](#TimeUnitTypeEnum) | The time unit. Along with num_time_units defines the amount of time over which impressions per user are counted and capped. |  [optional] |
|**timeUnitsCount** | **Integer** | The amount of time, in the units specified by time_unit_type. Defines the amount of time over which impressions per user are counted and capped. |  [optional] |



## Enum: TimeUnitTypeEnum

| Name | Value |
|---- | -----|
| TIME_UNIT_TYPE_UNSPECIFIED | &quot;TIME_UNIT_TYPE_UNSPECIFIED&quot; |
| MINUTE | &quot;MINUTE&quot; |
| HOUR | &quot;HOUR&quot; |
| DAY | &quot;DAY&quot; |
| WEEK | &quot;WEEK&quot; |
| MONTH | &quot;MONTH&quot; |
| LIFETIME | &quot;LIFETIME&quot; |
| POD | &quot;POD&quot; |
| STREAM | &quot;STREAM&quot; |



