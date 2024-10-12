# ThePlaidApi.Enhancements

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **[String]** | A hierarchical array of the categories to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget). | 
**categoryId** | **String** | The ID of the category to which this transaction belongs. For a full list of categories, see [&#x60;/categories/get&#x60;](https://plaid.com/docs/api/products/transactions/#categoriesget). | 
**checkNumber** | **String** | The check number of the transaction. This field is only populated for check transactions. | [optional] 
**counterparties** | [**[Counterparty]**](Counterparty.md) | The counterparties present in the transaction. Counterparties, such as the merchant or the financial institution, are extracted by Plaid from the raw description. | [optional] 
**location** | [**Location**](Location.md) |  | 
**logoUrl** | **String** | The URL of a logo associated with this transaction, if available. The logo is formatted as a 100x100 pixel PNG file. | [optional] 
**merchantName** | **String** | The name of the primary counterparty, such as the merchant or the financial institution, as extracted by Plaid from the raw description. | [optional] 
**paymentChannel** | [**PaymentChannel**](PaymentChannel.md) |  | 
**personalFinanceCategory** | [**PersonalFinanceCategory**](PersonalFinanceCategory.md) |  | [optional] 
**personalFinanceCategoryIconUrl** | **String** | A link to the icon associated with the primary personal finance category. The logo will always be 100x100 pixels. | [optional] 
**website** | **String** | The website associated with this transaction, if available. | [optional] 


