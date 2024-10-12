

# PayRun


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deductions** | **Double** | The total Deductions for the Payrun |  [optional] |
|**netPay** | **Double** | The total NetPay for the Payrun |  [optional] |
|**payRunID** | **UUID** | Xero identifier for pay run |  [optional] |
|**payRunPeriodEndDate** | **String** | Period End Date for the PayRun (YYYY-MM-DD) |  [optional] |
|**payRunPeriodStartDate** | **String** | Period Start Date for the PayRun (YYYY-MM-DD) |  [optional] |
|**payRunStatus** | **PayRunStatus** |  |  [optional] |
|**paymentDate** | **String** | Payment Date for the PayRun (YYYY-MM-DD) |  [optional] |
|**payrollCalendarID** | **UUID** | Xero identifier for pay run |  |
|**payslipMessage** | **String** | Payslip message for the PayRun |  [optional] |
|**payslips** | [**List&lt;PayslipSummary&gt;**](PayslipSummary.md) | The payslips in the payrun |  [optional] |
|**reimbursement** | **Double** | The total Reimbursements for the Payrun |  [optional] |
|**_super** | **Double** | The total Super for the Payrun |  [optional] |
|**tax** | **Double** | The total Tax for the Payrun |  [optional] |
|**updatedDateUTC** | **String** | Last modified timestamp |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |
|**wages** | **Double** | The total Wages for the Payrun |  [optional] |



