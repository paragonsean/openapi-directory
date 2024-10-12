

# ChartDataExtras


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**druidTimeOrigin** | **String** | Starting point for time grain counting on legacy Druid datasources. Used to change e.g. Monday/Sunday first-day-of-week. |  [optional] |
|**having** | **String** | HAVING clause to be added to aggregate queries using AND operator. |  [optional] |
|**havingDruid** | [**List&lt;ChartDataFilter&gt;**](ChartDataFilter.md) | HAVING filters to be added to legacy Druid datasource queries. |  [optional] |
|**relativeEnd** | [**RelativeEndEnum**](#RelativeEndEnum) | End time for relative time deltas. Default: &#x60;config[\&quot;DEFAULT_RELATIVE_START_TIME\&quot;]&#x60; |  [optional] |
|**relativeStart** | [**RelativeStartEnum**](#RelativeStartEnum) | Start time for relative time deltas. Default: &#x60;config[\&quot;DEFAULT_RELATIVE_START_TIME\&quot;]&#x60; |  [optional] |
|**timeGrainSqla** | [**TimeGrainSqlaEnum**](#TimeGrainSqlaEnum) | To what level of granularity should the temporal column be aggregated. Supports [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) durations. |  [optional] |
|**timeRangeEndpoints** | **List&lt;Object&gt;** |  |  [optional] |
|**where** | **String** | WHERE clause to be added to queries using AND operator. |  [optional] |



## Enum: RelativeEndEnum

| Name | Value |
|---- | -----|
| TODAY | &quot;today&quot; |
| NOW | &quot;now&quot; |



## Enum: RelativeStartEnum

| Name | Value |
|---- | -----|
| TODAY | &quot;today&quot; |
| NOW | &quot;now&quot; |



## Enum: TimeGrainSqlaEnum

| Name | Value |
|---- | -----|
| PT1_S | &quot;PT1S&quot; |
| PT5_S | &quot;PT5S&quot; |
| PT30_S | &quot;PT30S&quot; |
| PT1_M | &quot;PT1M&quot; |
| PT5_M | &quot;PT5M&quot; |
| PT10_M | &quot;PT10M&quot; |
| PT15_M | &quot;PT15M&quot; |
| PT0_5_H | &quot;PT0.5H&quot; |
| PT1_H | &quot;PT1H&quot; |
| PT6_H | &quot;PT6H&quot; |
| P1_D | &quot;P1D&quot; |
| P1_W | &quot;P1W&quot; |
| P1_M | &quot;P1M&quot; |
| P0_25_Y | &quot;P0.25Y&quot; |
| P1_Y | &quot;P1Y&quot; |
| _1969_12_28_T00_00_00_Z_P1_W | &quot;1969-12-28T00:00:00Z/P1W&quot; |
| _1969_12_29_T00_00_00_Z_P1_W | &quot;1969-12-29T00:00:00Z/P1W&quot; |
| P1_W_1970_01_03_T00_00_00_Z | &quot;P1W/1970-01-03T00:00:00Z&quot; |
| P1_W_1970_01_04_T00_00_00_Z | &quot;P1W/1970-01-04T00:00:00Z&quot; |



