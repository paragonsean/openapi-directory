# ThePlaidApi.TransactionStream

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | The ID of the account to which the stream belongs | 
**averageAmount** | [**TransactionStreamAmount**](TransactionStreamAmount.md) |  | 
**category** | **[String]** | A hierarchical array of the categories to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget). | 
**categoryId** | **String** | The ID of the category to which this transaction belongs. See [Categories](https://plaid.com/docs/api/products/transactions/#categoriesget). | 
**description** | **String** | A description of the transaction stream. | 
**firstDate** | **Date** | The posted date of the earliest transaction in the stream. | 
**frequency** | [**RecurringTransactionFrequency**](RecurringTransactionFrequency.md) |  | 
**isActive** | **Boolean** | Indicates whether the transaction stream is still live. | 
**lastAmount** | [**TransactionStreamAmount**](TransactionStreamAmount.md) |  | 
**lastDate** | **Date** | The posted date of the latest transaction in the stream. | 
**merchantName** | **String** | The merchant associated with the transaction stream. | 
**personalFinanceCategory** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | [optional] 
**status** | [**TransactionStreamStatus**](TransactionStreamStatus.md) |  | 
**streamId** | **String** | A unique id for the stream | 
**transactionIds** | **[String]** | An array of Plaid transaction IDs belonging to the stream, sorted by posted date. | 


