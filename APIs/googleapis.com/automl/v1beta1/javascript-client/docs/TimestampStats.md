# CloudAutoMlApi.TimestampStats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**granularStats** | [**{String: GranularStats}**](GranularStats.md) | The string key is the pre-defined granularity. Currently supported: hour_of_day, day_of_week, month_of_year. Granularities finer that the granularity of timestamp data are not populated (e.g. if timestamps are at day granularity, then hour_of_day is not populated). | [optional] 


