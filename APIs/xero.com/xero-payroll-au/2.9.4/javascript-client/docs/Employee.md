# XeroPayrollAuApi.Employee

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankAccounts** | [**[BankAccount]**](BankAccount.md) |  | [optional] 
**classification** | **String** | Employees classification | [optional] 
**dateOfBirth** | **String** | Date of birth of the employee (YYYY-MM-DD) | 
**email** | **String** | The email address for the employee | [optional] 
**employeeGroupName** | **String** | The Employee Group allows you to report on payroll expenses and liabilities for each group of employees | [optional] 
**employeeID** | **String** | Xero unique identifier for an Employee | [optional] 
**firstName** | **String** | First name of employee | 
**gender** | **String** | The employee’s gender. See Employee Gender | [optional] 
**homeAddress** | [**HomeAddress**](HomeAddress.md) |  | [optional] 
**isAuthorisedToApproveLeave** | **Boolean** | Authorised to approve other employees&#39; leave requests | [optional] 
**isAuthorisedToApproveTimesheets** | **Boolean** | Authorised to approve timesheets | [optional] 
**jobTitle** | **String** | JobTitle of the employee | [optional] 
**lastName** | **String** | Last name of employee | 
**leaveBalances** | [**[LeaveBalance]**](LeaveBalance.md) |  | [optional] 
**leaveLines** | [**[LeaveLine]**](LeaveLine.md) |  | [optional] 
**middleNames** | **String** | Middle name(s) of the employee | [optional] 
**mobile** | **String** | Employee mobile number | [optional] 
**openingBalances** | [**OpeningBalances**](OpeningBalances.md) |  | [optional] 
**ordinaryEarningsRateID** | **String** | Xero unique identifier for earnings rate | [optional] 
**payTemplate** | [**PayTemplate**](PayTemplate.md) |  | [optional] 
**payrollCalendarID** | **String** | Xero unique identifier for payroll calendar for the employee | [optional] 
**phone** | **String** | Employee phone number | [optional] 
**startDate** | **String** | Start date for an employee (YYYY-MM-DD) | [optional] 
**status** | [**EmployeeStatus**](EmployeeStatus.md) |  | [optional] 
**superMemberships** | [**[SuperMembership]**](SuperMembership.md) |  | [optional] 
**taxDeclaration** | [**TaxDeclaration**](TaxDeclaration.md) |  | [optional] 
**terminationDate** | **String** | Employee Termination Date (YYYY-MM-DD) | [optional] 
**title** | **String** | Title of the employee | [optional] 
**twitterUserName** | **String** | Employee’s twitter name | [optional] 
**updatedDateUTC** | **String** | Last modified timestamp | [optional] [readonly] 
**validationErrors** | [**[ValidationError]**](ValidationError.md) | Displays array of validation error messages from the API | [optional] 



## Enum: GenderEnum


* `N` (value: `"N"`)

* `M` (value: `"M"`)

* `F` (value: `"F"`)

* `I` (value: `"I"`)




