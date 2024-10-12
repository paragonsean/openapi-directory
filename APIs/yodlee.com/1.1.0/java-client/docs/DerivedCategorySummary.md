

# DerivedCategorySummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**categoryId** | **Long** | Id of the category. This information is provided by transactions/categories service.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; |  [optional] [readonly] |
|**categoryName** | **String** | The name of the category.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; |  [optional] [readonly] |
|**creditTotal** | [**Money**](Money.md) |  |  [optional] |
|**debitTotal** | [**Money**](Money.md) |  |  [optional] |
|**details** | [**List&lt;DerivedCategorySummaryDetails&gt;**](DerivedCategorySummaryDetails.md) | Credit and debit summary per date.&lt;br&gt;&lt;br&gt;&lt;b&gt;Applicable containers&lt;/b&gt;: creditCard, bank, investment&lt;br&gt; |  [optional] [readonly] |
|**links** | [**DerivedTransactionsLinks**](DerivedTransactionsLinks.md) |  |  [optional] |



