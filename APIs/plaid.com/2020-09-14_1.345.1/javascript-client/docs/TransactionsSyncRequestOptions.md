# ThePlaidApi.TransactionsSyncRequestOptions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**includeLogoAndCounterpartyBeta** | **Boolean** | Include counterparties and extra merchant fields in the transaction. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager. | [optional] [default to false]
**includeOriginalDescription** | **Boolean** | Include the raw unparsed transaction description from the financial institution. This field is disabled by default. If you need this information in addition to the parsed data provided, contact your Plaid Account Manager or submit a [Support request](https://dashboard.plaid.com/support/new/product-and-development/product-troubleshooting/product-functionality). | [optional] [default to false]
**includePersonalFinanceCategory** | **Boolean** | Include the [&#x60;personal_finance_category&#x60;](https://plaid.com/docs/api/products/transactions/#transactions-sync-response-added-personal-finance-category) object in the response.  See the [&#x60;taxonomy csv file&#x60;](https://plaid.com/documents/transactions-personal-finance-category-taxonomy.csv) for a full list of personal finance categories.  We’re introducing Category Rules - a new beta endpoint that will enable you to change the &#x60;personal_finance_category&#x60; for a transaction based on your users’ needs. When rules are set, the selected category will override the Plaid provided category. To learn more, send a note to transactions-feedback@plaid.com. | [optional] [default to false]


