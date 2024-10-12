# ThePlaidApi.TransactionsRulesCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessToken** | **String** | The access token associated with the Item data is being requested for. | 
**clientId** | **String** | Your Plaid API &#x60;client_id&#x60;. The &#x60;client_id&#x60; is required and may be provided either in the &#x60;PLAID-CLIENT-ID&#x60; header or as part of a request body. | [optional] 
**personalFinanceCategory** | **String** | Personal finance detailed category.  See the [&#x60;taxonomy csv file&#x60;](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.  | 
**ruleDetails** | [**TransactionsRuleDetails**](TransactionsRuleDetails.md) |  | 
**secret** | **String** | Your Plaid API &#x60;secret&#x60;. The &#x60;secret&#x60; is required and may be provided either in the &#x60;PLAID-SECRET&#x60; header or as part of a request body. | [optional] 


