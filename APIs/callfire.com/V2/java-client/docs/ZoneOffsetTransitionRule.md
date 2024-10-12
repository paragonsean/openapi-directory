

# ZoneOffsetTransitionRule

~

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dayOfMonthIndicator** | **Integer** | ~ |  [optional] |
|**dayOfWeek** | [**DayOfWeekEnum**](#DayOfWeekEnum) | ~ |  [optional] |
|**_localTime** | [**ModelLocalTime**](ModelLocalTime.md) |  |  [optional] |
|**midnightEndOfDay** | **Boolean** | ~ |  [optional] |
|**month** | [**MonthEnum**](#MonthEnum) | ~ |  [optional] |
|**offsetAfter** | [**ZoneOffset**](ZoneOffset.md) |  |  [optional] |
|**offsetBefore** | [**ZoneOffset**](ZoneOffset.md) |  |  [optional] |
|**standardOffset** | [**ZoneOffset**](ZoneOffset.md) |  |  [optional] |
|**timeDefinition** | [**TimeDefinitionEnum**](#TimeDefinitionEnum) | ~ |  [optional] |



## Enum: DayOfWeekEnum

| Name | Value |
|---- | -----|
| MONDAY | &quot;MONDAY&quot; |
| TUESDAY | &quot;TUESDAY&quot; |
| WEDNESDAY | &quot;WEDNESDAY&quot; |
| THURSDAY | &quot;THURSDAY&quot; |
| FRIDAY | &quot;FRIDAY&quot; |
| SATURDAY | &quot;SATURDAY&quot; |
| SUNDAY | &quot;SUNDAY&quot; |



## Enum: MonthEnum

| Name | Value |
|---- | -----|
| JANUARY | &quot;JANUARY&quot; |
| FEBRUARY | &quot;FEBRUARY&quot; |
| MARCH | &quot;MARCH&quot; |
| APRIL | &quot;APRIL&quot; |
| MAY | &quot;MAY&quot; |
| JUNE | &quot;JUNE&quot; |
| JULY | &quot;JULY&quot; |
| AUGUST | &quot;AUGUST&quot; |
| SEPTEMBER | &quot;SEPTEMBER&quot; |
| OCTOBER | &quot;OCTOBER&quot; |
| NOVEMBER | &quot;NOVEMBER&quot; |
| DECEMBER | &quot;DECEMBER&quot; |



## Enum: TimeDefinitionEnum

| Name | Value |
|---- | -----|
| UTC | &quot;UTC&quot; |
| WALL | &quot;WALL&quot; |
| STANDARD | &quot;STANDARD&quot; |



