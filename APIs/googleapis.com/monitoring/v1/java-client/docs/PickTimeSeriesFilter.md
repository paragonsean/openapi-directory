

# PickTimeSeriesFilter

Describes a ranking-based time series filter. Each input time series is ranked with an aligner. The filter will allow up to num_time_series time series to pass through it, selecting them based on the relative ranking.For example, if ranking_method is METHOD_MEAN,direction is BOTTOM, and num_time_series is 3, then the 3 times series with the lowest mean values will pass through the filter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**direction** | [**DirectionEnum**](#DirectionEnum) | How to use the ranking to select time series that pass through the filter. |  [optional] |
|**interval** | [**Interval**](Interval.md) |  |  [optional] |
|**numTimeSeries** | **Integer** | How many time series to allow to pass through the filter. |  [optional] |
|**rankingMethod** | [**RankingMethodEnum**](#RankingMethodEnum) | ranking_method is applied to each time series independently to produce the value which will be used to compare the time series to other time series. |  [optional] |



## Enum: DirectionEnum

| Name | Value |
|---- | -----|
| DIRECTION_UNSPECIFIED | &quot;DIRECTION_UNSPECIFIED&quot; |
| TOP | &quot;TOP&quot; |
| BOTTOM | &quot;BOTTOM&quot; |



## Enum: RankingMethodEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;METHOD_UNSPECIFIED&quot; |
| MEAN | &quot;METHOD_MEAN&quot; |
| MAX | &quot;METHOD_MAX&quot; |
| MIN | &quot;METHOD_MIN&quot; |
| SUM | &quot;METHOD_SUM&quot; |
| LATEST | &quot;METHOD_LATEST&quot; |



