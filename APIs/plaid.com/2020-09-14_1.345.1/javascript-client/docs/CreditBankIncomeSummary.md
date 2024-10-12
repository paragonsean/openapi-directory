# ThePlaidApi.CreditBankIncomeSummary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endDate** | **Date** | The latest date in which all income sources identified by Plaid appear in the user&#39;s account. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**historicalSummary** | [**[CreditBankIncomeHistoricalSummary]**](CreditBankIncomeHistoricalSummary.md) |  | [optional] 
**incomeCategoriesCount** | **Number** | Number of income categories per end user. | [optional] 
**incomeSourcesCount** | **Number** | Number of income sources per end user. | [optional] 
**incomeTransactionsCount** | **Number** | Number of income transactions per end user. | [optional] 
**isoCurrencyCode** | **String** | The ISO 4217 currency code of the amount or balance. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 
**startDate** | **Date** | The earliest date within the days requested in which all income sources identified by Plaid appear in a user&#39;s account. The date will be returned in an ISO 8601 format (YYYY-MM-DD). | [optional] 
**totalAmount** | **Number** | Total amount of earnings across all the income sources in the end user&#39;s Items for the days requested by the client. This may return an incorrect value if the summary includes income sources in multiple currencies. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 
**totalAmounts** | [**[CreditAmountWithCurrency]**](CreditAmountWithCurrency.md) | Total amount of earnings across all the income sources in the end user&#39;s Items for the days requested by the client. This can contain multiple amounts, with each amount denominated in one unique currency. | [optional] 
**unofficialCurrencyCode** | **String** | The unofficial currency code associated with the amount or balance. Always &#x60;null&#x60; if &#x60;iso_currency_code&#x60; is non-null. Unofficial currency codes are used for currencies that do not have official ISO currency codes, such as cryptocurrencies and the currencies of certain countries. Please use [&#x60;total_amounts&#x60;](https://plaid.com/docs/api/products/income/#credit-bank_income-get-response-bank-income-bank-income-summary-total-amounts) instead. | [optional] 


