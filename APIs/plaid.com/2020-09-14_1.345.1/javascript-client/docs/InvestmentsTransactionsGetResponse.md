# ThePlaidApi.InvestmentsTransactionsGetResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accounts** | [**[AccountBase]**](AccountBase.md) | The accounts for which transaction history is being fetched. | 
**investmentTransactions** | [**[InvestmentTransaction]**](InvestmentTransaction.md) | The transactions being fetched | 
**item** | [**Item**](Item.md) |  | 
**requestId** | **String** | A unique identifier for the request, which can be used for troubleshooting. This identifier, like all Plaid identifiers, is case sensitive. | 
**securities** | [**[Security]**](Security.md) | All securities for which there is a corresponding transaction being fetched. | 
**totalInvestmentTransactions** | **Number** | The total number of transactions available within the date range specified. If &#x60;total_investment_transactions&#x60; is larger than the size of the &#x60;transactions&#x60; array, more transactions are available and can be fetched via manipulating the &#x60;offset&#x60; parameter. | 


