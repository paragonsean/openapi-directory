

# DataSourceRefreshSchedule

Schedule for refreshing the data source. Data sources in the spreadsheet are refreshed within a time interval. You can specify the start time by clicking the Scheduled Refresh button in the Sheets editor, but the interval is fixed at 4 hours. For example, if you specify a start time of 8 AM , the refresh will take place between 8 AM and 12 PM every day.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dailySchedule** | [**DataSourceRefreshDailySchedule**](DataSourceRefreshDailySchedule.md) |  |  [optional] |
|**enabled** | **Boolean** | True if the refresh schedule is enabled, or false otherwise. |  [optional] |
|**monthlySchedule** | [**DataSourceRefreshMonthlySchedule**](DataSourceRefreshMonthlySchedule.md) |  |  [optional] |
|**nextRun** | [**Interval**](Interval.md) |  |  [optional] |
|**refreshScope** | [**RefreshScopeEnum**](#RefreshScopeEnum) | The scope of the refresh. Must be ALL_DATA_SOURCES. |  [optional] |
|**weeklySchedule** | [**DataSourceRefreshWeeklySchedule**](DataSourceRefreshWeeklySchedule.md) |  |  [optional] |



## Enum: RefreshScopeEnum

| Name | Value |
|---- | -----|
| DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED | &quot;DATA_SOURCE_REFRESH_SCOPE_UNSPECIFIED&quot; |
| ALL_DATA_SOURCES | &quot;ALL_DATA_SOURCES&quot; |



