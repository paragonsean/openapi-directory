

# MonthlySchedule

Represents a monthly schedule. An example of a valid monthly schedule is \"on the third Tuesday of the month\" or \"on the 15th of the month\".

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**monthDay** | **Integer** | Required. One day of the month. 1-31 indicates the 1st to the 31st day. -1 indicates the last day of the month. Months without the target day will be skipped. For example, a schedule to run \&quot;every month on the 31st\&quot; will not run in February, April, June, etc. |  [optional] |
|**weekDayOfMonth** | [**WeekDayOfMonth**](WeekDayOfMonth.md) |  |  [optional] |



