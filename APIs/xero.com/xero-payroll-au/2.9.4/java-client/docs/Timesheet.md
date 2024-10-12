

# Timesheet


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**employeeID** | **UUID** | The Xero identifier for an employee |  |
|**endDate** | **String** | Period end date (YYYY-MM-DD) |  |
|**hours** | **Double** | Timesheet total hours |  [optional] |
|**startDate** | **String** | Period start date (YYYY-MM-DD) |  |
|**status** | **TimesheetStatus** |  |  [optional] |
|**timesheetID** | **UUID** | The Xero identifier for a Payroll Timesheet |  [optional] |
|**timesheetLines** | [**List&lt;TimesheetLine&gt;**](TimesheetLine.md) |  |  [optional] |
|**updatedDateUTC** | **String** | Last modified timestamp |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



