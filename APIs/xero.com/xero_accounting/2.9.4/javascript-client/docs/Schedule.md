# XeroAccountingApi.Schedule

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dueDate** | **Number** | Integer used with due date type e.g 20 (of following month), 31 (of current month) | [optional] 
**dueDateType** | **String** | the payment terms | [optional] 
**endDate** | **String** | Invoice end date – only returned if the template has an end date set | [optional] 
**nextScheduledDate** | **String** | The calendar date of the next invoice in the schedule to be generated | [optional] 
**period** | **Number** | Integer used with the unit e.g. 1 (every 1 week), 2 (every 2 months) | [optional] 
**startDate** | **String** | Date the first invoice of the current version of the repeating schedule was generated (changes when repeating invoice is edited) | [optional] 
**unit** | **String** | One of the following - WEEKLY or MONTHLY | [optional] 



## Enum: DueDateTypeEnum


* `DAYSAFTERBILLDATE` (value: `"DAYSAFTERBILLDATE"`)

* `DAYSAFTERBILLMONTH` (value: `"DAYSAFTERBILLMONTH"`)

* `DAYSAFTERINVOICEDATE` (value: `"DAYSAFTERINVOICEDATE"`)

* `DAYSAFTERINVOICEMONTH` (value: `"DAYSAFTERINVOICEMONTH"`)

* `OFCURRENTMONTH` (value: `"OFCURRENTMONTH"`)

* `OFFOLLOWINGMONTH` (value: `"OFFOLLOWINGMONTH"`)





## Enum: UnitEnum


* `WEEKLY` (value: `"WEEKLY"`)

* `MONTHLY` (value: `"MONTHLY"`)




