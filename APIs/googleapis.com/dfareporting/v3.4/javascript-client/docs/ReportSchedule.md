# CampaignManager360Api.ReportSchedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Whether the schedule is active or not. Must be set to either true or false. | [optional] 
**every** | **Number** | Defines every how many days, weeks or months the report should be run. Needs to be set when \&quot;repeats\&quot; is either \&quot;DAILY\&quot;, \&quot;WEEKLY\&quot; or \&quot;MONTHLY\&quot;. | [optional] 
**expirationDate** | **Date** |  | [optional] 
**repeats** | **String** | The interval for which the report is repeated. Note: - \&quot;DAILY\&quot; also requires field \&quot;every\&quot; to be set. - \&quot;WEEKLY\&quot; also requires fields \&quot;every\&quot; and \&quot;repeatsOnWeekDays\&quot; to be set. - \&quot;MONTHLY\&quot; also requires fields \&quot;every\&quot; and \&quot;runsOnDayOfMonth\&quot; to be set.  | [optional] 
**repeatsOnWeekDays** | **[String]** | List of week days \&quot;WEEKLY\&quot; on which scheduled reports should run. | [optional] 
**runsOnDayOfMonth** | **String** | Enum to define for \&quot;MONTHLY\&quot; scheduled reports whether reports should be repeated on the same day of the month as \&quot;startDate\&quot; or the same day of the week of the month. Example: If &#39;startDate&#39; is Monday, April 2nd 2012 (2012-04-02), \&quot;DAY_OF_MONTH\&quot; would run subsequent reports on the 2nd of every Month, and \&quot;WEEK_OF_MONTH\&quot; would run subsequent reports on the first Monday of the month. | [optional] 
**startDate** | **Date** |  | [optional] 



## Enum: [RepeatsOnWeekDaysEnum]


* `SUNDAY` (value: `"SUNDAY"`)

* `MONDAY` (value: `"MONDAY"`)

* `TUESDAY` (value: `"TUESDAY"`)

* `WEDNESDAY` (value: `"WEDNESDAY"`)

* `THURSDAY` (value: `"THURSDAY"`)

* `FRIDAY` (value: `"FRIDAY"`)

* `SATURDAY` (value: `"SATURDAY"`)





## Enum: RunsOnDayOfMonthEnum


* `DAY_OF_MONTH` (value: `"DAY_OF_MONTH"`)

* `WEEK_OF_MONTH` (value: `"WEEK_OF_MONTH"`)




