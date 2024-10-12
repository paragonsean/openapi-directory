

# Compensation


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**benefits** | [**List&lt;Benefit&gt;**](Benefit.md) | An array of employee benefits for the pay period. |  [optional] |
|**deductions** | [**List&lt;Deduction&gt;**](Deduction.md) | An array of employee deductions for the pay period. |  [optional] |
|**employeeId** | **String** | A unique identifier for an object. |  [readonly] |
|**grossPay** | **BigDecimal** | The employee&#39;s gross pay. Only available when payroll has been processed |  [optional] |
|**netPay** | **BigDecimal** | The employee&#39;s net pay. Only available when payroll has been processed |  [optional] |
|**taxes** | [**List&lt;Tax&gt;**](Tax.md) | An array of employer and employee taxes for the pay period. |  [optional] |



