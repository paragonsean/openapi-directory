# XeroPayrollAuApi.Timesheet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employeeID** | **String** | The Xero identifier for an employee | 
**endDate** | **String** | Period end date (YYYY-MM-DD) | 
**hours** | **Number** | Timesheet total hours | [optional] 
**startDate** | **String** | Period start date (YYYY-MM-DD) | 
**status** | [**TimesheetStatus**](TimesheetStatus.md) |  | [optional] 
**timesheetID** | **String** | The Xero identifier for a Payroll Timesheet | [optional] 
**timesheetLines** | [**[TimesheetLine]**](TimesheetLine.md) |  | [optional] 
**updatedDateUTC** | **String** | Last modified timestamp | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 


