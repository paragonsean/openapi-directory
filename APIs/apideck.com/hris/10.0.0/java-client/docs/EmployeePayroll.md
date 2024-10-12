

# EmployeePayroll


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**checkDate** | **String** | The date on which employees will be paid for the payroll. |  |
|**companyId** | **String** | The unique identifier of the company. |  [optional] |
|**compensations** | [**List&lt;Compensation&gt;**](Compensation.md) | An array of compensations for the payroll. |  [optional] |
|**employeeId** | **String** | ID of the employee |  [optional] |
|**endDate** | **String** | The end date, inclusive, of the pay period. |  |
|**id** | **String** | A unique identifier for an object. |  [readonly] |
|**processed** | **Boolean** | Whether or not the payroll has been successfully processed. Note that processed payrolls cannot be updated. |  |
|**processedDate** | **String** | The date the payroll was processed. |  [optional] |
|**startDate** | **String** | The start date, inclusive, of the pay period. |  |
|**totals** | **PayrollTotals** |  |  [optional] |



