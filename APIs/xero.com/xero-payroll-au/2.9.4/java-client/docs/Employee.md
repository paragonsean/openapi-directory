

# Employee


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bankAccounts** | [**List&lt;BankAccount&gt;**](BankAccount.md) |  |  [optional] |
|**classification** | **String** | Employees classification |  [optional] |
|**dateOfBirth** | **String** | Date of birth of the employee (YYYY-MM-DD) |  |
|**email** | **String** | The email address for the employee |  [optional] |
|**employeeGroupName** | **String** | The Employee Group allows you to report on payroll expenses and liabilities for each group of employees |  [optional] |
|**employeeID** | **UUID** | Xero unique identifier for an Employee |  [optional] |
|**firstName** | **String** | First name of employee |  |
|**gender** | [**GenderEnum**](#GenderEnum) | The employee’s gender. See Employee Gender |  [optional] |
|**homeAddress** | [**HomeAddress**](HomeAddress.md) |  |  [optional] |
|**isAuthorisedToApproveLeave** | **Boolean** | Authorised to approve other employees&#39; leave requests |  [optional] |
|**isAuthorisedToApproveTimesheets** | **Boolean** | Authorised to approve timesheets |  [optional] |
|**jobTitle** | **String** | JobTitle of the employee |  [optional] |
|**lastName** | **String** | Last name of employee |  |
|**leaveBalances** | [**List&lt;LeaveBalance&gt;**](LeaveBalance.md) |  |  [optional] |
|**leaveLines** | [**List&lt;LeaveLine&gt;**](LeaveLine.md) |  |  [optional] |
|**middleNames** | **String** | Middle name(s) of the employee |  [optional] |
|**mobile** | **String** | Employee mobile number |  [optional] |
|**openingBalances** | [**OpeningBalances**](OpeningBalances.md) |  |  [optional] |
|**ordinaryEarningsRateID** | **UUID** | Xero unique identifier for earnings rate |  [optional] |
|**payTemplate** | [**PayTemplate**](PayTemplate.md) |  |  [optional] |
|**payrollCalendarID** | **UUID** | Xero unique identifier for payroll calendar for the employee |  [optional] |
|**phone** | **String** | Employee phone number |  [optional] |
|**startDate** | **String** | Start date for an employee (YYYY-MM-DD) |  [optional] |
|**status** | **EmployeeStatus** |  |  [optional] |
|**superMemberships** | [**List&lt;SuperMembership&gt;**](SuperMembership.md) |  |  [optional] |
|**taxDeclaration** | [**TaxDeclaration**](TaxDeclaration.md) |  |  [optional] |
|**terminationDate** | **String** | Employee Termination Date (YYYY-MM-DD) |  [optional] |
|**title** | **String** | Title of the employee |  [optional] |
|**twitterUserName** | **String** | Employee’s twitter name |  [optional] |
|**updatedDateUTC** | **String** | Last modified timestamp |  [optional] [readonly] |
|**validationErrors** | [**List&lt;ValidationError&gt;**](ValidationError.md) | Displays array of validation error messages from the API |  [optional] |



## Enum: GenderEnum

| Name | Value |
|---- | -----|
| N | &quot;N&quot; |
| M | &quot;M&quot; |
| F | &quot;F&quot; |
| I | &quot;I&quot; |



