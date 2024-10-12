# Superset.ChartDataExtras

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**druidTimeOrigin** | **String** | Starting point for time grain counting on legacy Druid datasources. Used to change e.g. Monday/Sunday first-day-of-week. | [optional] 
**having** | **String** | HAVING clause to be added to aggregate queries using AND operator. | [optional] 
**havingDruid** | [**[ChartDataFilter]**](ChartDataFilter.md) | HAVING filters to be added to legacy Druid datasource queries. | [optional] 
**relativeEnd** | **String** | End time for relative time deltas. Default: &#x60;config[\&quot;DEFAULT_RELATIVE_START_TIME\&quot;]&#x60; | [optional] 
**relativeStart** | **String** | Start time for relative time deltas. Default: &#x60;config[\&quot;DEFAULT_RELATIVE_START_TIME\&quot;]&#x60; | [optional] 
**timeGrainSqla** | **String** | To what level of granularity should the temporal column be aggregated. Supports [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Durations) durations. | [optional] 
**timeRangeEndpoints** | **[Object]** |  | [optional] 
**where** | **String** | WHERE clause to be added to queries using AND operator. | [optional] 



## Enum: RelativeEndEnum


* `today` (value: `"today"`)

* `now` (value: `"now"`)





## Enum: RelativeStartEnum


* `today` (value: `"today"`)

* `now` (value: `"now"`)





## Enum: TimeGrainSqlaEnum


* `PT1S` (value: `"PT1S"`)

* `PT5S` (value: `"PT5S"`)

* `PT30S` (value: `"PT30S"`)

* `PT1M` (value: `"PT1M"`)

* `PT5M` (value: `"PT5M"`)

* `PT10M` (value: `"PT10M"`)

* `PT15M` (value: `"PT15M"`)

* `PT0.5H` (value: `"PT0.5H"`)

* `PT1H` (value: `"PT1H"`)

* `PT6H` (value: `"PT6H"`)

* `P1D` (value: `"P1D"`)

* `P1W` (value: `"P1W"`)

* `P1M` (value: `"P1M"`)

* `P0.25Y` (value: `"P0.25Y"`)

* `P1Y` (value: `"P1Y"`)

* `1969-12-28T00:00:00Z/P1W` (value: `"1969-12-28T00:00:00Z/P1W"`)

* `1969-12-29T00:00:00Z/P1W` (value: `"1969-12-29T00:00:00Z/P1W"`)

* `P1W/1970-01-03T00:00:00Z` (value: `"P1W/1970-01-03T00:00:00Z"`)

* `P1W/1970-01-04T00:00:00Z` (value: `"P1W/1970-01-04T00:00:00Z"`)




