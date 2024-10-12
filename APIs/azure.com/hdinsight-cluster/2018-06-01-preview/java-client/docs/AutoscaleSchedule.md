

# AutoscaleSchedule

Parameters for a schedule-based autoscale rule, consisting of an array of days + a time and capacity

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**days** | [**List&lt;DaysEnum&gt;**](#List&lt;DaysEnum&gt;) | Days of the week for a schedule-based autoscale rule |  [optional] |
|**timeAndCapacity** | [**AutoscaleTimeAndCapacity**](AutoscaleTimeAndCapacity.md) |  |  [optional] |



## Enum: List&lt;DaysEnum&gt;

| Name | Value |
|---- | -----|
| MONDAY | &quot;Monday&quot; |
| TUESDAY | &quot;Tuesday&quot; |
| WEDNESDAY | &quot;Wednesday&quot; |
| THURSDAY | &quot;Thursday&quot; |
| FRIDAY | &quot;Friday&quot; |
| SATURDAY | &quot;Saturday&quot; |
| SUNDAY | &quot;Sunday&quot; |



