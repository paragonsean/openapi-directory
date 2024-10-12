# HrisApi.Compensation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**benefits** | [**[Benefit]**](Benefit.md) | An array of employee benefits for the pay period. | [optional] 
**deductions** | [**[Deduction]**](Deduction.md) | An array of employee deductions for the pay period. | [optional] 
**employeeId** | **String** | A unique identifier for an object. | [readonly] 
**grossPay** | **Number** | The employee&#39;s gross pay. Only available when payroll has been processed | [optional] 
**netPay** | **Number** | The employee&#39;s net pay. Only available when payroll has been processed | [optional] 
**taxes** | [**[Tax]**](Tax.md) | An array of employer and employee taxes for the pay period. | [optional] 


