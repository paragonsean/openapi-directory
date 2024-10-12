# ThePlaidApi.LinkTokenCreateRequestIncomeVerificationPayrollIncome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flowTypes** | [**[IncomeVerificationPayrollFlowType]**](IncomeVerificationPayrollFlowType.md) | The types of payroll income verification to enable for the Link session. If none are specified, then users will see both document and digital payroll income. | [optional] 
**isUpdateMode** | **Boolean** | An identifier to indicate whether the income verification Link token will be used for an update or not | [optional] [default to false]
**itemIdToUpdate** | **String** | Uniquely identify a payroll income item to update with. It should only be used for update mode. | [optional] 


