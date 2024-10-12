# CampaignManager360Api.DayPartTargeting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**daysOfWeek** | **[String]** | Days of the week when the ad will serve. Acceptable values are: - \&quot;SUNDAY\&quot; - \&quot;MONDAY\&quot; - \&quot;TUESDAY\&quot; - \&quot;WEDNESDAY\&quot; - \&quot;THURSDAY\&quot; - \&quot;FRIDAY\&quot; - \&quot;SATURDAY\&quot;  | [optional] 
**hoursOfDay** | **[Number]** | Hours of the day when the ad will serve, where 0 is midnight to 1 AM and 23 is 11 PM to midnight. Can be specified with days of week, in which case the ad would serve during these hours on the specified days. For example if Monday, Wednesday, Friday are the days of week specified and 9-10am, 3-5pm (hours 9, 15, and 16) is specified, the ad would serve Monday, Wednesdays, and Fridays at 9-10am and 3-5pm. Acceptable values are 0 to 23, inclusive. | [optional] 
**userLocalTime** | **Boolean** | Whether or not to use the user&#39;s local time. If false, the America/New York time zone applies. | [optional] 



## Enum: [DaysOfWeekEnum]


* `MONDAY` (value: `"MONDAY"`)

* `TUESDAY` (value: `"TUESDAY"`)

* `WEDNESDAY` (value: `"WEDNESDAY"`)

* `THURSDAY` (value: `"THURSDAY"`)

* `FRIDAY` (value: `"FRIDAY"`)

* `SATURDAY` (value: `"SATURDAY"`)

* `SUNDAY` (value: `"SUNDAY"`)




