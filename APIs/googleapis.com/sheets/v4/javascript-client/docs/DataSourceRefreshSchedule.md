# GoogleSheetsApi.DataSourceRefreshSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dailySchedule** | [**DataSourceRefreshDailySchedule**](DataSourceRefreshDailySchedule.md) |  | [optional] 
**enabled** | **Boolean** | True if the refresh schedule is enabled, or false otherwise. | [optional] 
**monthlySchedule** | [**DataSourceRefreshMonthlySchedule**](DataSourceRefreshMonthlySchedule.md) |  | [optional] 
**nextRun** | [**Interval**](Interval.md) |  | [optional] 
**refreshScope** | **String** | The scope of the refresh. Must be ALL_DATA_SOURCES. | [optional] 
**weeklySchedule** | [**DataSourceRefreshWeeklySchedule**](DataSourceRefreshWeeklySchedule.md) |  | [optional] 



## Enum: RefreshScopeEnum


* `DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED` (value: `"DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED"`)

* `ALL_DATA_SOURCES` (value: `"ALL_DATA_SOURCES"`)




