

# Schedule


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**dueDate** | **Integer** | Integer used with due date type e.g 20 (of following month), 31 (of current month) |  [optional] |
|**dueDateType** | [**DueDateTypeEnum**](#DueDateTypeEnum) | the payment terms |  [optional] |
|**endDate** | **String** | Invoice end date – only returned if the template has an end date set |  [optional] |
|**nextScheduledDate** | **String** | The calendar date of the next invoice in the schedule to be generated |  [optional] |
|**period** | **Integer** | Integer used with the unit e.g. 1 (every 1 week), 2 (every 2 months) |  [optional] |
|**startDate** | **String** | Date the first invoice of the current version of the repeating schedule was generated (changes when repeating invoice is edited) |  [optional] |
|**unit** | [**UnitEnum**](#UnitEnum) | One of the following - WEEKLY or MONTHLY |  [optional] |



## Enum: DueDateTypeEnum

| Name | Value |
|---- | -----|
| DAYSAFTERBILLDATE | &quot;DAYSAFTERBILLDATE&quot; |
| DAYSAFTERBILLMONTH | &quot;DAYSAFTERBILLMONTH&quot; |
| DAYSAFTERINVOICEDATE | &quot;DAYSAFTERINVOICEDATE&quot; |
| DAYSAFTERINVOICEMONTH | &quot;DAYSAFTERINVOICEMONTH&quot; |
| OFCURRENTMONTH | &quot;OFCURRENTMONTH&quot; |
| OFFOLLOWINGMONTH | &quot;OFFOLLOWINGMONTH&quot; |



## Enum: UnitEnum

| Name | Value |
|---- | -----|
| WEEKLY | &quot;WEEKLY&quot; |
| MONTHLY | &quot;MONTHLY&quot; |



