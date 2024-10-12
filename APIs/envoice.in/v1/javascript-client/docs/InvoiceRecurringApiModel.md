# ApiV100.InvoiceRecurringApiModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dayOfMonth** | **Number** | Day of month when the recurrance should happen | [optional] 
**dayOfWeek** | **String** | Day when the recurrance should happen | [optional] 
**dueDateInDays** | **Number** | Total number of days for the client to pay the invoice after issuing it | [optional] 
**endOfRecurrance** | **Date** | Indcate the date when the recurrance should stop | [optional] 
**month** | **Number** | Month when the recurrance should happen | [optional] 
**recurrancePattern** | **String** | How often the recurrance occurs | [optional] 
**recurranceValue** | **Number** | Recurring every [value] RecurrancePattern  Ex: Recur every 1 week | [optional] 
**startOfRecurrance** | **Date** | Indcate the date when the recurrance has started | [optional] 
**status** | **String** | The status of the recurrance | [optional] 
**title** | **String** | Title of the recurring profile.   Ex: BRAND PACKAGE - 2017-08-16 - 2018-08-16 | [optional] 



## Enum: DayOfWeekEnum


* `Sunday` (value: `"Sunday"`)

* `Monday` (value: `"Monday"`)

* `Tuesday` (value: `"Tuesday"`)

* `Wednesday` (value: `"Wednesday"`)

* `Thursday` (value: `"Thursday"`)

* `Friday` (value: `"Friday"`)

* `Saturday` (value: `"Saturday"`)





## Enum: RecurrancePatternEnum


* `Daily` (value: `"Daily"`)

* `Weekly` (value: `"Weekly"`)

* `Monthly` (value: `"Monthly"`)

* `Yearly` (value: `"Yearly"`)





## Enum: StatusEnum


* `Pending` (value: `"Pending"`)

* `Active` (value: `"Active"`)

* `Cancelled` (value: `"Cancelled"`)

* `Finished` (value: `"Finished"`)




