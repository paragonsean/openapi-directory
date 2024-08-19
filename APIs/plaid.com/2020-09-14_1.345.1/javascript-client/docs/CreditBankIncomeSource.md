# ThePlaidApi.CreditBankIncomeSource

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | Plaid&#39;s unique identifier for the account. | [optional] 
**endDate** | **Date** | Maximum of all dates within the specific income sources in the user’s bank account for days requested by the client. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**historicalSummary** | [**[CreditBankIncomeHistoricalSummary]**](CreditBankIncomeHistoricalSummary.md) |  | [optional] 
**incomeCategory** | [**CreditBankIncomeCategory**](CreditBankIncomeCategory.md) |  | [optional] 
**incomeDescription** | **String** | The most common name or original description for the underlying income transactions. | [optional] 
**incomeSourceId** | **String** | A unique identifier for an income source. | [optional] 
**payFrequency** | [**CreditBankIncomePayFrequency**](CreditBankIncomePayFrequency.md) |  | [optional] 
**startDate** | **Date** | Minimum of all dates within the specific income sources in the user&#39;s bank account for days requested by the client. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**totalAmount** | **Number** | Total amount of earnings in the user’s bank account for the specific income source for days requested by the client. | [optional] 
**transactionCount** | **Number** | Number of transactions for the income source within the start and end date. | [optional] 


