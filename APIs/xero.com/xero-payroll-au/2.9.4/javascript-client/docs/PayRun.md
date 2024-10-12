# XeroPayrollAuApi.PayRun

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deductions** | **Number** | The total Deductions for the Payrun | [optional] 
**netPay** | **Number** | The total NetPay for the Payrun | [optional] 
**payRunID** | **String** | Xero identifier for pay run | [optional] 
**payRunPeriodEndDate** | **String** | Period End Date for the PayRun (YYYY-MM-DD) | [optional] 
**payRunPeriodStartDate** | **String** | Period Start Date for the PayRun (YYYY-MM-DD) | [optional] 
**payRunStatus** | [**PayRunStatus**](PayRunStatus.md) |  | [optional] 
**paymentDate** | **String** | Payment Date for the PayRun (YYYY-MM-DD) | [optional] 
**payrollCalendarID** | **String** | Xero identifier for pay run | 
**payslipMessage** | **String** | Payslip message for the PayRun | [optional] 
**payslips** | [**[PayslipSummary]**](PayslipSummary.md) | The payslips in the payrun | [optional] 
**reimbursement** | **Number** | The total Reimbursements for the Payrun | [optional] 
**_super** | **Number** | The total Super for the Payrun | [optional] 
**tax** | **Number** | The total Tax for the Payrun | [optional] 
**updatedDateUTC** | **String** | Last modified timestamp | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 
**wages** | **Number** | The total Wages for the Payrun | [optional] 


