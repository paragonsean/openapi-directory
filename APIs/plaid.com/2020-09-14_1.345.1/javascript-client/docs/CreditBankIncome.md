# ThePlaidApi.CreditBankIncome

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bankIncomeId** | **String** | The unique identifier associated with the Bank Income Report. | [optional] 
**bankIncomeSummary** | [**CreditBankIncomeSummary**](CreditBankIncomeSummary.md) |  | [optional] 
**daysRequested** | **Number** | The number of days requested by the customer for the Bank Income Report. | [optional] 
**generatedTime** | **Date** | The time when the Bank Income Report was generated. | [optional] 
**items** | [**[CreditBankIncomeItem]**](CreditBankIncomeItem.md) | The list of Items in the report along with the associated metadata about the Item. | [optional] 
**warnings** | [**[CreditBankIncomeWarning]**](CreditBankIncomeWarning.md) | If data from the Bank Income report was unable to be retrieved, the warnings will contain information about the error that caused the data to be incomplete. | [optional] 


