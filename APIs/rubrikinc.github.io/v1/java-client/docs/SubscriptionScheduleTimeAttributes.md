

# SubscriptionScheduleTimeAttributes


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dailyScheduleHour** | **Integer** | Hour of the day to send the scheduled email, if the user picks a daily schedule. 0 &#x3D; 12AM, 23 &#x3D; 11PM. |  [optional] |
|**dayOfMonth** | **Integer** | Day of the month to send the scheduled email, if the user picks a monthly schedule. |  [optional] |
|**daysOfWeek** | **List&lt;Integer&gt;** | Day of the week, represented by numbers, to send the scheduled email, if the user picks a weekly schedule. 0 &#x3D; Sunday, 1 &#x3D; Monday, 2 &#x3D; Tuesday, 3 &#x3D; Wednesday, 4 &#x3D; Thursday, 5 &#x3D; Friday, 6 &#x3D; Saturday. |  [optional] |
|**monthlyScheduleHour** | **Integer** | Hour of the user-specified day to send the scheduled email, if the user picks a monthly schedule. 0 &#x3D; 12AM, 23 &#x3D; 11PM. |  [optional] |
|**weeklyScheduleHour** | **Integer** | Hour of the user-specified day to send the scheduled email, if the user picks a weekly schedule. 0 &#x3D; 12AM, 23 &#x3D; 11PM. |  [optional] |



