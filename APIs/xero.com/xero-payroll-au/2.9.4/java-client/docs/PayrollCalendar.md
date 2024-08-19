

# PayrollCalendar


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**calendarType** | **CalendarType** |  |  [optional] |
|**name** | **String** | Name of the Payroll Calendar |  [optional] |
|**paymentDate** | **String** | The date on which employees will be paid for the upcoming pay period (YYYY-MM-DD) |  [optional] |
|**payrollCalendarID** | **UUID** | Xero identifier |  [optional] |
|**startDate** | **String** | The start date of the upcoming pay period. The end date will be calculated based upon this date, and the calendar type selected (YYYY-MM-DD) |  [optional] |
|**updatedDateUTC** | **String** | Last modified timestamp |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



